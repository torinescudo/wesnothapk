/*
	Copyright (C) 2025
	by Subhraman Sarkar (babaissarkar) <sbmskmm@protonmail.com>
	Part of the Battle for Wesnoth Project https://www.wesnoth.org/

	This program is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation; either version 2 of the License, or
	(at your option) any later version.
	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY.

	See the COPYING file for more details.
*/

package org.wesnoth.Wesnoth;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FilterInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.zip.ZipEntry;
import java.util.zip.ZipException;
import java.util.zip.ZipFile;
import java.util.zip.ZipInputStream;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.Intent;
import android.content.res.AssetFileDescriptor;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.PowerManager;
import android.os.StatFs;
import android.provider.Settings;
import android.util.Log;
import android.view.DisplayCutout;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.view.WindowInsets;
import android.view.WindowInsetsController;
import android.view.WindowManager;
import android.view.animation.AnimationUtils;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.PopupMenu;
import android.widget.ProgressBar;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.documentfile.provider.DocumentFile;

public class InitActivity extends Activity {
	private final static String MANIFEST_URL =
		"https://sourceforge.net/projects/wesnoth/files/wesnoth/wesnoth-%s/android-data/manifest.txt/download";

	private File dataDir;
	private Properties status = new Properties();
	private boolean launchTutorial;
	private String launchCampaign;
	private AlertDialog dialog;

	private String toSizeString(long bytes) {
		return String.format("%4.2f MB", (bytes * 1.0f) / (1e6));
	}

	@Override
	protected void onCreate(Bundle savedState) {
		super.onCreate(savedState);
		setContentView(R.layout.activity_init);

		// Keep the screen on while this activity runs
		getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);

		keepContentOutOfCutouts();
		((TextView) findViewById(R.id.app_version))
			.setText(getString(R.string.phone_version, BuildConfig.VERSION_NAME));

		initMainDataDir();
		
		status = initStatusFile(new File(dataDir, "status.properties"));

		initSettingsMenu();

		doPowerCheckAndStart();
	}

	private int dp(int value) {
		return Math.round(value * getResources().getDisplayMetrics().density);
	}

	/**
	 * The launcher is fullscreen in landscape, so a notch or a rounded corner can
	 * sit over the top corners where the settings button lives. Reserving the
	 * cutout insets as padding keeps every control inside the usable area.
	 */
	private void keepContentOutOfCutouts() {
		View screen = findViewById(R.id.screen);
		screen.setOnApplyWindowInsetsListener((view, insets) -> {
			int left = 0, top = 0, right = 0, bottom = 0;
			if (Build.VERSION.SDK_INT >= 28) {
				DisplayCutout cutout = insets.getDisplayCutout();
				if (cutout != null) {
					left = cutout.getSafeInsetLeft();
					top = cutout.getSafeInsetTop();
					right = cutout.getSafeInsetRight();
					bottom = cutout.getSafeInsetBottom();
				}
			}
			view.setPadding(left, top, right, bottom);
			return insets;
		});
	}
	
	/**
	 * Enforces immersive fullscreen on every focus gain.
	 * Needed because system UI can reappear after notifications/dialogs.
	 * API 30+: hides insets and extends content behind system bars.
	 * API <30: uses legacy immersive sticky flags with layout flags to
	 *           prevent gray padding where bars used to be.
	 */
	@Override
	public void onWindowFocusChanged(boolean hasFocus) {
		// hide system bars, navigation buttons, insets
		super.onWindowFocusChanged(hasFocus);
		if (hasFocus) {
			if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
				getWindow().setDecorFitsSystemWindows(false);
				getWindow().getInsetsController().hide(
					WindowInsets.Type.statusBars() | WindowInsets.Type.navigationBars()
				);
				getWindow().getInsetsController().setSystemBarsBehavior(
					WindowInsetsController.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE
				);
			} else {
				getWindow().getDecorView().setSystemUiVisibility(
					View.SYSTEM_UI_FLAG_FULLSCREEN
					| View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
					| View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
					| View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
					| View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
					| View.SYSTEM_UI_FLAG_LAYOUT_STABLE
				);
			}
		}
	}

	private List<PackageInfo> readManifest() {
		List<PackageInfo> packages = new ArrayList<>();
		long lastModified = Long.parseLong(status.getProperty("manifest.modified", "0"));
		
		String versionID = BuildConfig.VERSION_NAME;
		// Delete '+dev', since SF data url doesn't have it.
		if (versionID.endsWith("+dev")) {
			versionID = versionID.substring(0, versionID.length() - 4);
		}

		String downloadAddr = String.format(MANIFEST_URL, versionID);
		Log.d("Manifest", "Fetching manifest from " + downloadAddr);
		File manifestFile = new File(dataDir, "manifest.txt");
		
		try {
			lastModified = downloadFile(downloadAddr, manifestFile, lastModified, getString(R.string.phone_checking), true);

			Properties manifest = new Properties();
			manifest.load(new FileInputStream(manifestFile));
			for (String pkgid : manifest.getProperty("packages", "").split(",\\s*")) {
				packages.add(PackageInfo.from(manifest, pkgid));
			}
			Log.d("Manifest", "Last Modified: " + lastModified);
			Log.d("Manifest", "Packages: " + packages.toString());

			status.setProperty("manifest.modified", "" + lastModified);
			Log.d("Manifest", "Fetched and loaded successfully");
		} catch (Exception e) {
			Log.e("Download", "security error", e);
		}
		
		return packages;
	}

	public void onActivityResult(int reqCode, int resCode, Intent intent) {
		// Start the asset download only after the user has returned from
		// battery save settings, if they already went there via the
		// AlertDialog in onCreate().
		if (reqCode == 1) {
			initialize();
		} else if (reqCode == 2 && resCode == RESULT_OK) {
			initializeAssetsFromZip(intent.getData());
		} else if (reqCode == 3 && resCode == RESULT_OK) {
			importUserData(intent.getData());
		} else if (reqCode == 4 && resCode == RESULT_OK) {
			exportUserData(intent.getData());
		}
	}

	// Create the settings menu ui
	private void initSettingsMenu() {
		ImageButton btnSettings = findViewById(R.id.settings_btn);
		btnSettings.setOnClickListener(e -> {
			PopupMenu settingsMenu = new PopupMenu(InitActivity.this, btnSettings);
			settingsMenu.getMenuInflater().inflate(R.menu.main_menu, settingsMenu.getMenu());
			settingsMenu.setOnMenuItemClickListener(menuItem -> {
				if (menuItem.getItemId() == R.id.mnuClear) {
					// TODO do the deleting in another thread
					showClearDataDialog(dataDir);
					return true;
				} else if (menuItem.getItemId() == R.id.mnuLocalInstall) {
					showZIPHelpDialog();
					return true;
				} else if (menuItem.getItemId() == R.id.mnuImportExport) {
					showImportExportDialog();
					return true;
				}
				return false;
			});
			settingsMenu.show();
		});
	}

	// Note: wrap in runOnUiThread(()-> {...}) if called from another thread
	private void showLaunchScreen() {
		findViewById(R.id.settings_btn).setEnabled(true);
		findViewById(R.id.download_progress).setVisibility(View.INVISIBLE);
		findViewById(R.id.download_msg).setVisibility(View.INVISIBLE);
		TextView lblTap = findViewById(R.id.tap_label);
		lblTap.setText(R.string.phone_play);
		lblTap.setVisibility(View.VISIBLE);
		findViewById(R.id.phone_tutorial).setVisibility(View.VISIBLE);
		findViewById(R.id.phone_campaigns).setVisibility(View.VISIBLE);
	}

	// Note: wrap in runOnUiThread(()-> {...}) if called from another thread
	private void showProgressScreen() {
		findViewById(R.id.settings_btn).setEnabled(false);
		TextView lblTap = findViewById(R.id.tap_label);
		lblTap.clearAnimation();
		lblTap.setVisibility(View.INVISIBLE);
		findViewById(R.id.phone_tutorial).setVisibility(View.GONE);
		findViewById(R.id.phone_campaigns).setVisibility(View.GONE);
		findViewById(R.id.download_msg).setVisibility(View.VISIBLE);
		findViewById(R.id.download_progress).setVisibility(View.VISIBLE);
	}

	// Check if battery saver is on, and prompt to turn off
	// then start the main task
	private void doPowerCheckAndStart() {
		PowerManager powerManager = (PowerManager) getSystemService(Context.POWER_SERVICE);
		if (powerManager.isPowerSaveMode()) {
			new AlertDialog.Builder(this)
				.setTitle(R.string.phone_power_title)
				.setMessage(R.string.phone_power_message)
				// onActivityResult will be called (with reqCode = 1)
				// after this intent finishes, that is,
				// the user returns from Battery Saver settings
				.setPositiveButton(R.string.phone_power_settings, (dialog, which) -> startActivityForResult(new Intent(Settings.ACTION_BATTERY_SAVER_SETTINGS), 1))
				.setNegativeButton(R.string.phone_power_ignore, (dialog, which) -> initialize())
				.setCancelable(false)
				.show();
		} else {
			initialize();
		}
	}

	// Initialize gamedata directory
	private void initMainDataDir() {
		dataDir = new File(getExternalFilesDir(null), "gamedata");
		if (!dataDir.exists()) {
			dataDir.mkdir();
		}
		Log.d("InitActivity", "Creating " + dataDir);
	}

	private void initialize() {
		runOnUiThread(()-> {
			showLaunchScreen();
			findViewById(R.id.tap_label).setOnClickListener(e -> {
				launchTutorial = false;
				launchCampaign = null;
				initializeAssets();
			});
			findViewById(R.id.phone_tutorial).setOnClickListener(e -> {
				launchTutorial = true;
				launchCampaign = null;
				initializeAssets();
			});
			findViewById(R.id.phone_campaigns).setOnClickListener(e -> showCampaignPicker());
		});
	}

	/**
	 * Lists the bundled stories with their protagonist, length and hook, so the
	 * choice is made before the game has to load a main menu. Titles stay in the
	 * language the campaigns are written in.
	 */
	private void showCampaignPicker() {
		String[] titles = getResources().getStringArray(R.array.phone_campaign_titles);
		String[] meta = getResources().getStringArray(R.array.phone_campaign_meta);
		String[] hooks = getResources().getStringArray(R.array.phone_campaign_hooks);
		int count = Math.min(PhoneCampaigns.IDS.length, titles.length);

		LinearLayout list = new LinearLayout(this);
		list.setOrientation(LinearLayout.VERTICAL);
		list.setPadding(dp(10), dp(10), dp(10), dp(10));

		TextView intro = new TextView(this);
		intro.setText(R.string.phone_campaigns_intro);
		intro.setTextSize(13);
		intro.setTextColor(getColor(R.color.phone_text_muted));
		intro.setPadding(dp(6), dp(2), dp(6), dp(10));
		list.addView(intro);

		LayoutInflater inflater = LayoutInflater.from(this);
		for (int i = 0; i < count; ++i) {
			final String campaign = PhoneCampaigns.IDS[i];
			View row = inflater.inflate(R.layout.phone_campaign_item, list, false);
			((TextView) row.findViewById(R.id.phone_campaign_title)).setText(titles[i]);
			((TextView) row.findViewById(R.id.phone_campaign_meta)).setText(entry(meta, i));
			((TextView) row.findViewById(R.id.phone_campaign_hook)).setText(entry(hooks, i));
			row.setOnClickListener(view -> {
				dismissDialog();
				launchTutorial = false;
				launchCampaign = campaign;
				initializeAssets();
			});
			list.addView(row);
		}

		ScrollView scroll = new ScrollView(this);
		scroll.addView(list);
		dialog = new AlertDialog.Builder(this)
			.setTitle(R.string.phone_campaigns_title)
			.setView(scroll)
			.setNegativeButton(android.R.string.cancel, null)
			.create();
		dialog.show();
		stretchToScreen(dialog);
	}

	private String entry(String[] values, int index) {
		return index < values.length ? values[index] : "";
	}

	private void dismissDialog() {
		if (dialog != null) {
			dialog.dismiss();
			dialog = null;
		}
	}

	/** Keeps a long picker scrollable in landscape instead of running off screen. */
	private void stretchToScreen(AlertDialog target) {
		Window window = target.getWindow();
		if (window == null) return;
		window.setLayout(ViewGroup.LayoutParams.MATCH_PARENT,
			Math.round(getResources().getDisplayMetrics().heightPixels * 0.85f));
	}

	private void initializeAssets() {
		findViewById(R.id.screen).setOnClickListener(null);
		showProgressScreen();
		TextView progressText = findViewById(R.id.download_msg);
		progressText.setText(R.string.phone_preparing);

		if (bundledInstallPending() && !hasRoomForBundledData()) {
			return;
		}

		Executors.newSingleThreadExecutor().execute(() -> {
			try {
				if (installBundledData()) {
					extractNetworkCertificate();
					storeStatus(status);
					runOnUiThread(() -> launchWesnoth());
					return;
				}
			} catch (IOException failure) {
				Log.e("InitActivity", "Bundled data installation failed", failure);
				runOnUiThread(() -> new AlertDialog.Builder(this)
					.setTitle(R.string.phone_install_failed)
					.setMessage(R.string.phone_install_retry)
					.setPositiveButton(R.string.phone_retry, (d, which) -> initialize())
					.setNegativeButton(android.R.string.cancel, (d, which) -> finish())
					.show());
				return;
			}
			//TODO Update mechanism when patch is available.
			if (!Boolean.parseBoolean(status.getProperty("manual_install", "false"))) {
				HashMap<String, String> excluded = new HashMap<String, String>();
				
				for (PackageInfo info : readManifest()) {
					String id = info.getId();
					if (excluded.containsKey(id) && excluded.get(id).equals(info.getVersion())) {
						Log.d("InitActivity", "Not downloading excluded package " + id);
						continue;
					}
					
					String url = info.getURL();
					long lastModified = Long.parseLong(status.getProperty(id + ".modified", "0"));
					int oldVersion = PackageInfo.getPatchVersion(status.getProperty(id + ".version", "0"));
					int newVersion = info.getPatchVersion();
					boolean downloadPkg = newVersion > oldVersion;
					
					// Check if dependencies for this package exist, only download if all satisfied
					for (Map.Entry<String, String> dep : info.getDependencies().entrySet()) {
						int depOldVersion = PackageInfo.getPatchVersion(status.getProperty(dep.getKey() + ".version", "0"));
						int depNewVersion = PackageInfo.getPatchVersion(dep.getValue());
						if (depNewVersion != depOldVersion) {
							Log.d("InitActivity", "Dependency " + dep.getKey() + "for " + id + " not found");
							downloadPkg = false;
						}
					}
					
					Log.d("InitActivity", id + " version: " + oldVersion + " (local), " + newVersion + " (remote)");
					
					if (downloadPkg) {
						
						File packageFile = new File(dataDir, id + ".zip");
						
						// Download package
						Log.d("InitActivity", "Starting to download " + id + " from " + url);
						
						try {
							lastModified = downloadFile(
								url, packageFile, lastModified, info.getUIName(), false);
							
							status.setProperty(id + ".modified", "" + lastModified);
						} catch (Exception e) {
							Log.e("Download", "security error", e);
						}
	
						// Unpack archive
						// TODO Checksum verification?
						if (packageFile.exists()) {
							Log.d("InitActivity", "Start unpacking " + id);
							
							if (unpackArchive(packageFile, dataDir, info.getUIName())) {
								status.setProperty(id + ".version", "" + info.getVersion());
								// this package is already supplying what it excludes,
								// so mark excluded packages as installed
								for (Map.Entry<String, String> entry : info.getExcluded().entrySet()) {
									status.setProperty(entry.getKey() + ".version", entry.getValue().toString());
								}
								excluded.putAll(info.getExcluded());
								packageFile.delete();
							}
						}
					} else {
						Log.d("InitActivity", "No new version/dependency unmet for " + id + " found in server, skipping.");
					}
				}
			} else {
				Log.d("InitActivity", "Manually installed data, automatic updates will not be performed.");
			}

			extractNetworkCertificate();

			storeStatus(status);

			Log.d("InitActivity", "Stop unpack");

			if (new File(dataDir, "data").exists()
				&& new File(dataDir, "fonts").exists()
				&& new File(dataDir, "sounds").exists()
				&& new File(dataDir, "images").exists())
			{
				// Launch Wesnoth
				runOnUiThread(() -> launchWesnoth());
			} else {
				runOnUiThread(() -> {
					new AlertDialog.Builder(this)
						.setTitle(R.string.phone_data_missing_title)
						.setMessage(R.string.phone_data_missing_message)
						.setPositiveButton(R.string.phone_data_missing_download, (d, res) -> initialize())
						.setNegativeButton(R.string.phone_exit, (d, res) -> System.exit(0))
						.setCancelable(false)
						.show();
				});
			}
		});
	}

	private void launchWesnoth() {
		getWindow().clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
		TextView progressText = findViewById(R.id.download_msg);
		progressText.setText(R.string.phone_launching);
		Log.d("InitActivity", "Launch wesnoth");
		Intent launchIntent = new Intent(this, WesnothActivity.class);
		launchIntent.putExtra("phone_tutorial", launchTutorial);
		launchIntent.putExtra("phone_campaign", launchCampaign);
		launchIntent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
		startActivity(launchIntent);
		finish();
	}

	private Properties initStatusFile(File statusFile) {
		Properties status = new Properties();
		try (FileInputStream statusStream = new FileInputStream(statusFile)) {
			if (statusFile.exists()) {
				status.load(statusStream);
			} else {
				statusFile.createNewFile();
			}
		} catch (IOException ioe) {
			Log.e("InitActivity", "IO exception", ioe);
		}
		return status;
	}

	private void storeStatus(Properties status) {
		File statusFile = new File(dataDir, "status.properties");
		try (FileOutputStream statusStream = new FileOutputStream(statusFile)) {
			status.store(statusStream, "Wesnoth Assets Status");
		} catch (IOException ioe) {
			Log.e("InitActivity", "IO exception", ioe);
		}
	}

	// Extract certificate file from apk raw resource
	private void extractNetworkCertificate() {
		// TODO update mechanism for this file
		File certDir = new File(dataDir, "certificates");
		if (!certDir.exists()) {
			certDir.mkdir();
		}
		File certFile = new File(certDir, "cacert.pem");
		if (certFile.exists()) {
			return;
		}

		try (FileOutputStream certStream = new FileOutputStream(certFile)) {
			certFile.createNewFile();
			IOUtils.copyStream(getResources().openRawResource(R.raw.cacert), certStream);
		} catch (Exception e) {
			Log.e("InitActivity", "Exception", e);
		}
	}

	private void initializeAssetsFromZip(Uri uri) {
		Executors.newSingleThreadExecutor().execute(() -> {
			runOnUiThread(() -> showProgressScreen());

			initMainDataDir();
			
			status = initStatusFile(new File(dataDir, "status.properties"));
			
			String msg;
			if (unpackArchive(uri, dataDir, getString(R.string.phone_game_data))) {
				status.setProperty("manual_install", "true");
				// if we have a custom status.properties bundled inside, merge it with `status`.
				status.putAll(initStatusFile(new File(dataDir, "status.properties")));
				status.setProperty("manual_install", "true");
				status.remove("bundled_data");
				storeStatus(status);
				msg = getString(R.string.phone_installed);
			} else {
				msg = getString(R.string.phone_install_failed_toast);
			}

			runOnUiThread(() -> {
				runOnUiThread(()-> Toast.makeText(this, msg, Toast.LENGTH_SHORT).show());
				recreate();
			});
		});
	}

	private void showClearDataDialog(File dataDir) {
		new AlertDialog.Builder(this)
			.setTitle(R.string.phone_clear_title)
			.setMessage(R.string.phone_clear_message)
			.setPositiveButton(R.string.phone_clear_confirm, (dialog, which) -> {
				Toast.makeText(this, R.string.phone_clear_working, Toast.LENGTH_SHORT).show();
				try {
					GameDataFiles.deleteTree(dataDir);
					Toast.makeText(this, R.string.phone_clear_done, Toast.LENGTH_SHORT).show();
					recreate();
				} catch (IOException ioe) {
					Log.e("InitActivity", "IO exception", ioe);
					Toast.makeText(this, R.string.phone_clear_failed, Toast.LENGTH_SHORT).show();
				}
			})
			.setNegativeButton(android.R.string.cancel, null)
			.setCancelable(false)
			.show();
	}

	private void showZIPHelpDialog() {
		new AlertDialog.Builder(this)
			.setTitle(R.string.phone_zip_title)
			.setMessage(R.string.phone_zip_message)
			.setPositiveButton(R.string.phone_zip_proceed, (dialog, which) -> openDataFile())
			.setNegativeButton(android.R.string.cancel, null)
			.setCancelable(false)
			.show();
	}

	// Show a file chooser to open a file
	private void openDataFile() {
		Intent inttOpen = new Intent(Intent.ACTION_GET_CONTENT);
		inttOpen.addCategory(Intent.CATEGORY_OPENABLE);
		inttOpen.setType("application/zip");
		inttOpen.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, false);
		Intent inttOpen2 = Intent.createChooser(inttOpen, getString(R.string.phone_zip_proceed));
		startActivityForResult(inttOpen2, 2);
	}
	
	private void showImportExportDialog() {
		new AlertDialog.Builder(this)
			.setTitle(R.string.phone_userdata_title)
			.setMessage(R.string.phone_userdata_message)
			.setPositiveButton(R.string.phone_import, (dialog, which) ->
				// Open directory picker to select import destination
				startActivityForResult(new Intent(Intent.ACTION_OPEN_DOCUMENT_TREE), 3)
			)
			.setNegativeButton(R.string.phone_export, (dialog, which) ->
				// Open directory picker to select export destination
				startActivityForResult(new Intent(Intent.ACTION_OPEN_DOCUMENT_TREE), 4)
			)
			.setNeutralButton(android.R.string.cancel, null)
			.setCancelable(false)
			.show();
	}
	
	private void importUserData(Uri uri) {
		Executors.newSingleThreadExecutor().execute(() -> {
			runOnUiThread(()-> showProgressScreen());
			DocumentFile targetDir = DocumentFile.fromTreeUri(this, uri);
			if (targetDir == null) return;
			for (DocumentFile child : targetDir.listFiles()) {
				if (!child.getName().equals("gamedata")) {
					final String name = child.getName();
					runOnUiThread(()-> updateProgress(getString(R.string.phone_importing, name), -1));
					IOUtils.copyRecursive(this, child, getExternalFilesDir(null));
				}
			}
			runOnUiThread(()-> showLaunchScreen());
			runOnUiThread(()-> Toast.makeText(this, R.string.phone_import_done, Toast.LENGTH_SHORT).show());
		});
	}
	
	private void exportUserData(Uri uri) {
		Executors.newSingleThreadExecutor().execute(() -> {
			runOnUiThread(()-> showProgressScreen());
			for (File child : getExternalFilesDir(null).listFiles()) {
				if (!child.getName().equals("gamedata")) {
					final String name = child.getName();
					runOnUiThread(()-> updateProgress(getString(R.string.phone_exporting, name), -1));
					IOUtils.copyRecursive(this, child, uri);
				}
			}
			runOnUiThread(()-> showLaunchScreen());
			runOnUiThread(()-> Toast.makeText(this, R.string.phone_export_done, Toast.LENGTH_SHORT).show());
		});
	}
	
	/** percent < 0 leaves the bar indeterminate, which is all a stream can report. */
	private void updateProgress(String progressMsg, int percent) {
		TextView progressText = (TextView) findViewById(R.id.download_msg);
		ProgressBar progressBar = (ProgressBar) findViewById(R.id.download_progress);
		progressBar.setMax(100);
		progressBar.setIndeterminate(percent < 0);
		if (percent >= 0) {
			progressBar.setProgress(percent);
		}
		progressText.setText(progressMsg);
	}

	private void updateDownloadProgress(long done, long total, String type) {
		if (total > 0) {
			int percent = (int) Math.min(100, done * 100 / total);
			updateProgress(getString(R.string.phone_downloading, type,
				toSizeString(done), toSizeString(total), percent), percent);
		} else {
			updateProgress(getString(R.string.phone_downloading_unknown, type, toSizeString(done)), -1);
		}
	}

	/**
	 * Bundled installs count archive bytes; ZIP installs count entries, because
	 * only the byte stream of the bundled archive has a usable total.
	 */
	private void updateUnpackProgress(long done, long total, String type, boolean bySize) {
		if (total <= 0) {
			updateProgress(getString(R.string.phone_unpacking_unknown, type, done), -1);
			return;
		}
		int percent = (int) Math.min(100, done * 100 / total);
		updateProgress(bySize
			? getString(R.string.phone_unpacking_bytes, type, toSizeString(done), toSizeString(total), percent)
			: getString(R.string.phone_unpacking, type, done, total, percent), percent);
	}

	private long downloadFile(String url, File destpath, long modified, String typeOrMsg, boolean isCustomMsg) {
		long newModified = 0;
		// based on https://stackoverflow.com/a/4896527/22060628
		Log.d("Download", "URL: " + url);

		try {
			HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
			conn.setRequestProperty("Accept", "*/*");
			conn.setRequestProperty("User-Agent", "Wget/1.13.4 (linux-gnu)");
			conn.setRequestMethod("GET");
			conn.setConnectTimeout(10000); // 10 seconds
			conn.setReadTimeout(10000);    // 10 seconds

			final int response = conn.getResponseCode();
			if (response != HttpURLConnection.HTTP_OK) {
				Log.e("Download", "Server returned response: " + response);
				return newModified;
			}

			newModified = conn.getLastModified();
			// File did not change on server, don't download.
			if (newModified == modified) {
				return newModified;
			}
			
			final long max = conn.getContentLength();

			// TODO rewrite to use copyStream function.
			long done = 0;
			int lastPercent = -1;
			byte[] buffer = new byte[8192];
			try (
				DataInputStream in = new DataInputStream(conn.getInputStream());
				OutputStream out = new FileOutputStream(destpath))
			{
				int length;
				while ((length = in.read(buffer)) > 0) {
					out.write(buffer, 0, length);
					done += length;
					int percent = max > 0 ? (int) Math.min(100, done * 100 / max) : -1;
					if (!isCustomMsg && percent != lastPercent) {
						lastPercent = percent;
						final long downloaded = done;
						runOnUiThread(() -> updateDownloadProgress(downloaded, max, typeOrMsg));
					}
				}
			}

			Log.d("Download", "Download success from URL: " + url);
			return newModified;

		} catch (MalformedURLException mue) {
			Log.e("Download", "Malformed url exception", mue);
		} catch (IOException ioe) {
			Log.e("Download", "IO exception", ioe);
		} catch (SecurityException se) {
			Log.e("Download", "Security exception", se);
		}

		return 0;
	}

	/** Bundled archive identity, or an exception when this build ships no data. */
	private String readBundledChecksum() throws IOException {
		try (BufferedReader reader = new BufferedReader(new InputStreamReader(
			getAssets().open("gamedata.zip.sha256"), StandardCharsets.UTF_8))) {
			String line = reader.readLine();
			if (line == null || !line.matches("[0-9a-f]{64}\\s+.+")) {
				throw new IOException("Invalid bundled data identity");
			}
			return line.substring(0, 64);
		}
	}

	private boolean manualInstallWithoutBundledData() {
		return Boolean.parseBoolean(status.getProperty("manual_install", "false"))
			&& !status.containsKey("bundled_data");
	}

	private boolean bundledDataUnpacked(String checksum) {
		return checksum.equals(status.getProperty("bundled_data"))
			&& new File(dataDir, "data/_main.cfg").isFile()
			&& new File(dataDir, "fonts").isDirectory();
	}

	/** Mirrors installBundledData's own conditions, so the space check never misfires. */
	private boolean bundledInstallPending() {
		if (manualInstallWithoutBundledData()) return false;
		try {
			return !bundledDataUnpacked(readBundledChecksum());
		} catch (IOException noBundledData) {
			return false; // Small development APKs import their data manually.
		}
	}

	/**
	 * Unpacking the bundled archive on a full phone would stop halfway and leave
	 * a partial game directory, so the space is checked before anything is written.
	 */
	private boolean hasRoomForBundledData() {
		long archiveSize = bundledArchiveSize();
		if (archiveSize <= 0) return true;
		long needed = archiveSize + archiveSize / 5;
		long free = new StatFs(dataDir.getAbsolutePath()).getAvailableBytes();
		if (free >= needed) return true;

		new AlertDialog.Builder(this)
			.setTitle(R.string.phone_storage_title)
			.setMessage(getString(R.string.phone_storage_message, toSizeString(needed), toSizeString(free)))
			.setPositiveButton(R.string.phone_storage_check, (dialog, which) -> initializeAssets())
			.setNegativeButton(android.R.string.cancel, (dialog, which) -> finish())
			.setCancelable(false)
			.show();
		return false;
	}

	/** Uncompressed asset length, or 0 when it cannot be read. */
	private long bundledArchiveSize() {
		try (AssetFileDescriptor descriptor = getAssets().openFd("gamedata.zip")) {
			return descriptor.getLength();
		} catch (IOException unreadable) {
			return 0;
		}
	}

	/** A completed installation is keyed by the checksum of the bundled archive. */
	private boolean installBundledData() throws IOException {
		if (manualInstallWithoutBundledData()) return false;
		String checksum;
		try {
			checksum = readBundledChecksum();
		} catch (FileNotFoundException absent) {
			return false; // Supports small development APKs with manual data import.
		}
		if (bundledDataUnpacked(checksum)) return true;

		try (InputStream archive = getAssets().open("gamedata.zip")) {
			// Only game data is replaced. Saves and preferences are sibling directories.
			GameDataFiles.deleteTree(dataDir);
			if (!dataDir.mkdirs()) throw new IOException("Cannot create game-data directory");
			status.clear();
			if (!unpackArchive(archive, dataDir, getString(R.string.phone_game_data), bundledArchiveSize())) {
				throw new IOException("Cannot unpack bundled game data");
			}
			status.setProperty("bundled_data", checksum);
			status.setProperty("manual_install", "false");
			storeStatus(status);
			return true;
		}
	}

	private boolean unpackArchive(Uri uri, File destdir, String type) {
		Log.d("Unpack", "Start");

		long total = -1;
		try (AssetFileDescriptor descriptor = getContentResolver().openAssetFileDescriptor(uri, "r")) {
			if (descriptor != null) total = descriptor.getLength();
		} catch (IOException | SecurityException unknownLength) {
			total = -1; // Providers may refuse; the bar stays indeterminate then.
		}

		InputStream zipstream = null;
		try {
			zipstream = getContentResolver().openInputStream(uri);
		} catch (FileNotFoundException fe) {
			Log.e("Unpack", "File not found exception", fe);
			return false;
		}
		return zipstream != null && unpackArchive(zipstream, destdir, type, total);
	}

	private boolean unpackArchive(InputStream zipstream, File destdir, String type, long totalBytes) {
		CountingInputStream counted = new CountingInputStream(zipstream);
		try (ZipInputStream zf = new ZipInputStream(counted)) {
			AtomicInteger progress = new AtomicInteger(1);
			int lastPercent = -1;

			runOnUiThread(() -> updateUnpackProgress(0, totalBytes, type, true));

			ZipEntry ze;
			while ((ze = zf.getNextEntry()) != null) {
				File destination = GameDataFiles.resolve(destdir, ze.getName());
				File directory = ze.isDirectory() ? destination : destination.getParentFile();
				if (!directory.isDirectory() && !directory.mkdirs()) {
					throw new IOException("Cannot create " + directory);
				}
				if (!ze.isDirectory()) {
					try (FileOutputStream out = new FileOutputStream(destination)) {
						IOUtils.copyStreamNoClose(zf, out);
					}
				}

				if (totalBytes > 0) {
					final long done = counted.count();
					int percent = (int) Math.min(100, done * 100 / totalBytes);
					if (percent != lastPercent) {
						lastPercent = percent;
						runOnUiThread(() -> updateUnpackProgress(done, totalBytes, type, true));
					}
				} else if (progress.get() % 100 == 1) {
					// No usable total: report how many entries have been written.
					final int completed = progress.get();
					runOnUiThread(() -> updateUnpackProgress(completed, 0, type, false));
				}

				progress.incrementAndGet();
			}
			
			boolean res = applyDeleteList();
			
			Log.d("Unpack", "Done unpacking " + type);
			
			return res;
		} catch (ZipException e) {
			Log.e("Unpack", "ZIP exception", e);
		} catch (FileNotFoundException e) {
			Log.e("Unpack", "File not found", e);
		} catch (IOException e) {
			Log.e("Unpack", "IO exception", e);
		}

		return false;
	}

	private boolean unpackArchive(File zipfile, File destdir, String type) {
		Log.d("Unpack", "Start");

		if (zipfile == null) {
			Log.e("Unpack", "File for " + type + " is null!");
			return false;
		}

		try (ZipFile zf = new ZipFile(zipfile)) {
			Enumeration<? extends ZipEntry> e = zf.entries();

			AtomicInteger progress = new AtomicInteger(1);
			final int max = zf.size();
			int lastPercent = -1;

			while (e.hasMoreElements()) {
				ZipEntry ze = (ZipEntry) e.nextElement();

				int percent = max > 0 ? (int) Math.min(100, progress.get() * 100 / max) : -1;
				if (percent != lastPercent) {
					lastPercent = percent;
					final long completed = progress.get();
					runOnUiThread(() -> updateUnpackProgress(completed, max, type, false));
				}

				if (ze.isDirectory()) {
					File dir = new File(destdir, ze.getName());
					if (!dir.exists()) {
						dir.mkdir();
					}
				} else {
					IOUtils.copyStream(
						zf.getInputStream(ze),
						new FileOutputStream(new File(destdir, ze.getName())));
				}

				Log.d("Unpack", "Unpacking " + type + ": " + progress.get() + "/" + max);
				progress.incrementAndGet();
			}

			boolean res = applyDeleteList();
			
			Log.d("Unpack", "Done unpacking " + type);
			
			return res;
		} catch (ZipException e) {
			Log.e("Unpack", "ZIP exception", e);
			return false;
		} catch (FileNotFoundException e) {
			Log.e("Unpack", "File not found", e);
			return false;
		} catch (IOException e) {
			Log.e("Unpack", "IO exception", e);
			return false;
		}
	}
	
	/**
	 * Delete any files on the deletelist file (delete.list on zip root)
	 * inside ZIP. Deletelist file will be deleted on success.
	 */
	private boolean applyDeleteList() {
		Log.d("InitActivity", "Applying deletelist");
		File deleteList = new File(dataDir, "delete.list");
		if (!deleteList.exists()) {
			 // Unpack finished sucessfully and no deletelist, so no deletion needed
			Log.d("InitActivity", "deletelist " + deleteList.getAbsolutePath() + " not found, skipping");
			return true;
		}
		
		AtomicInteger progress = new AtomicInteger(1);
		runOnUiThread(() -> updateProgress(getString(R.string.phone_patching, 0), -1));
		String line = "";
		try (BufferedReader reader = new BufferedReader(new InputStreamReader(
			new FileInputStream(deleteList), StandardCharsets.UTF_8))) {
			Log.d("Unpack", "Reading deletelist");
			while ((line = reader.readLine()) != null) {
				if (line.trim().isEmpty()) continue;
				File toDelete = GameDataFiles.resolve(dataDir, line);
				if (toDelete.exists()) {
					Log.d("Unpack", "Deleting " + toDelete.getAbsolutePath());
					if (!toDelete.delete()) throw new IOException("Cannot delete " + toDelete);
					final int applied = progress.incrementAndGet();
					runOnUiThread(() -> updateProgress(getString(R.string.phone_patching, applied), -1));
				} else {
					Log.d("Unpack", "File " + toDelete.getAbsolutePath() + " doesn't exist.");
				}
			}
			
			if (!deleteList.delete()) throw new IOException("Cannot remove applied delete list");
			return true;
		} catch (IOException e) {
			Log.e("Unpack", "Deleting " + line + " failed.");
		}
		
		return false;
	}

	/** Counts archive bytes as the unpacker consumes them, so the bar shows real progress. */
	private static final class CountingInputStream extends FilterInputStream {
		private long read;

		CountingInputStream(InputStream source) {
			super(source);
		}

		@Override public int read() throws IOException {
			int value = super.read();
			if (value >= 0) ++read;
			return value;
		}

		@Override public int read(byte[] buffer, int offset, int length) throws IOException {
			int count = super.read(buffer, offset, length);
			if (count > 0) read += count;
			return count;
		}

		long count() {
			return read;
		}
	}
}
