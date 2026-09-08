/* SPDX-License-Identifier: GPL-2.0-or-later */
package org.wesnoth.Wesnoth;

import android.app.AlertDialog;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Handler;
import android.os.Build;
import android.os.Looper;
import android.os.SystemClock;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.HorizontalScrollView;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.Toast;

/** Native-sized, accessible controls surrounding the SDL game surface. */
final class PhoneControls {
    // Wire IDs match src/phone_actions.hpp. No dependency on editable hotkeys.
    static final String[] ACTIONS = {
        "cycle", "recruit", "undo", "endturn", "zoomin", "zoomout",
        "objectives", "save", "recall", "unitlist", "leader", "describeunit",
        "preferences", "quit", "moveaction"
    };
    private static final int[] LABELS = {
        R.string.phone_next, R.string.phone_recruit, R.string.phone_undo,
        R.string.phone_end_turn, R.string.phone_zoom_in, R.string.phone_zoom_out,
        R.string.phone_objectives, R.string.phone_save, R.string.phone_recall,
        R.string.phone_units, R.string.phone_leader, R.string.phone_unit_info,
        R.string.phone_preferences, R.string.phone_quit, R.string.phone_move_action
    };

    private final WesnothActivity activity;
    private final View surface;
    private final LinearLayout bar;
    private final LinearLayout actions;
    private final Button toggle;
    private final Button more;
    private final Button[] buttons = new Button[ACTIONS.length];
    private final SharedPreferences settings;
    private final Handler handler = new Handler(Looper.getMainLooper());
    private boolean expanded;
    private boolean running;
    private int previousMask = Integer.MIN_VALUE;
    private int reservedHeight = -1;
    private AlertDialog dialog;

    PhoneControls(WesnothActivity activity, ViewGroup root, View surface) {
        this.activity = activity;
        this.surface = surface;
        settings = activity.getSharedPreferences("phone_controls", 0);
        expanded = settings.getBoolean("expanded", true);
        bar = new LinearLayout(activity);
        bar.setOrientation(LinearLayout.HORIZONTAL);
        bar.setGravity(Gravity.CENTER_VERTICAL);
        bar.setBackgroundColor(Color.rgb(24, 32, 39));
        bar.setPadding(dp(4), dp(2), dp(4), dp(2));
        bar.setVisibility(View.GONE);
        bar.setOnApplyWindowInsetsListener((view, insets) -> {
            int left = 0, right = 0, bottom = 0;
            if (Build.VERSION.SDK_INT >= 28 && insets.getDisplayCutout() != null) {
                left = insets.getDisplayCutout().getSafeInsetLeft();
                right = insets.getDisplayCutout().getSafeInsetRight();
                bottom = insets.getDisplayCutout().getSafeInsetBottom();
            }
            bar.setPadding(dp(4) + left, dp(2), dp(4) + right, dp(2) + bottom);
            return insets;
        });

        toggle = button(R.string.phone_controls);
        toggle.setOnClickListener(view -> {
            expanded = !expanded;
            settings.edit().putBoolean("expanded", expanded).apply();
            updateLayout(previousMask);
        });
        bar.addView(toggle);

        HorizontalScrollView scroll = new HorizontalScrollView(activity);
        scroll.setFillViewport(true);
        actions = new LinearLayout(activity);
        actions.setGravity(Gravity.CENTER_VERTICAL);
        scroll.addView(actions);
        bar.addView(scroll, new LinearLayout.LayoutParams(0,
            ViewGroup.LayoutParams.WRAP_CONTENT, 1));
        for (int id : new int[] {14, 0, 1, 2, 4, 5}) {
            final int action = id;
            buttons[id] = button(LABELS[id]);
            buttons[id].setOnClickListener(view -> send(action));
            actions.addView(buttons[id]);
        }
        more = button(R.string.phone_more);
        more.setOnClickListener(view -> showMore());
        bar.addView(more);
        buttons[3] = button(LABELS[3]);
        buttons[3].setTextColor(Color.rgb(255, 216, 128));
        buttons[3].setOnClickListener(view -> confirm(3));
        bar.addView(buttons[3]);

        RelativeLayout.LayoutParams params = new RelativeLayout.LayoutParams(
            ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        params.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM);
        root.addView(bar, params);
        bar.addOnLayoutChangeListener((v, l, t, r, b, ol, ot, or, ob) -> reserveSurface());
    }

    private int dp(int value) {
        return Math.round(value * activity.getResources().getDisplayMetrics().density);
    }

    private Button button(int label) {
        Button result = new Button(activity);
        result.setText(label);
        result.setContentDescription(activity.getString(label));
        result.setAllCaps(false);
        result.setTextSize(14);
        result.setMinHeight(dp(48));
        result.setMinimumHeight(dp(48));
        result.setMinWidth(dp(64));
        result.setTextColor(Color.WHITE);
        result.setPadding(dp(12), dp(4), dp(12), dp(4));
        return result;
    }

    private final Runnable poll = new Runnable() {
        @Override public void run() {
            if (!running) return;
            int mask = WesnothActivity.nativeGetPhoneActions();
            if (mask != previousMask) {
                previousMask = mask;
                for (int i = 0; i < buttons.length; ++i) {
                    if (buttons[i] != null) {
                        boolean enabled = mask >= 0 && (mask & (1 << i)) != 0;
                        buttons[i].setEnabled(enabled);
                        buttons[i].setAlpha(enabled ? 1f : 0.4f);
                    }
                }
                updateLayout(mask);
            }
            handler.postDelayed(this, 250);
        }
    };

    void resume() {
        if (running) return;
        running = true;
        handler.post(poll);
    }

    void pause() {
        running = false;
        handler.removeCallbacksAndMessages(null);
        if (dialog != null) {
            dialog.dismiss();
            dialog = null;
        }
    }

    private void updateLayout(int mask) {
        bar.setVisibility(mask >= 0 ? View.VISIBLE : View.GONE);
        toggle.setText(expanded ? R.string.phone_hide : R.string.phone_controls);
        toggle.setContentDescription(activity.getString(
            expanded ? R.string.phone_hide : R.string.phone_controls));
        ((View) actions.getParent()).setVisibility(expanded ? View.VISIBLE : View.GONE);
        buttons[3].setVisibility(expanded ? View.VISIBLE : View.GONE);
        more.setVisibility(expanded ? View.VISIBLE : View.GONE);
        RelativeLayout.LayoutParams params = (RelativeLayout.LayoutParams) bar.getLayoutParams();
        params.width = expanded ? ViewGroup.LayoutParams.MATCH_PARENT : ViewGroup.LayoutParams.WRAP_CONTENT;
        params.addRule(RelativeLayout.ALIGN_PARENT_END);
        bar.setLayoutParams(params);
        reserveSurface();
    }

    private void reserveSurface() {
        int height = bar.getVisibility() == View.VISIBLE && expanded ? bar.getHeight() : 0;
        if (height == reservedHeight) return;
        reservedHeight = height;
        // SDL receives the resized surface, keeping touch coordinates aligned.
        ViewGroup.MarginLayoutParams params = (ViewGroup.MarginLayoutParams) surface.getLayoutParams();
        params.bottomMargin = height;
        surface.setLayoutParams(params);
    }

    private void send(int action) {
        final long deadline = SystemClock.uptimeMillis() + 1000;
        handler.post(new Runnable() {
            @Override public void run() {
                if (!running) return;
                // Android 6 pauses SDL when a native dialog takes focus. Wait
                // for focus and a fresh game snapshot after dismissing it.
                if (activity.hasWindowFocus()
                    && WesnothActivity.nativeQueuePhoneAction(action)) return;
                if (SystemClock.uptimeMillis() < deadline) {
                    handler.postDelayed(this, 50);
                } else {
                    Toast.makeText(activity, R.string.phone_unavailable, Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    private void confirm(int action) {
        dialog = new AlertDialog.Builder(activity)
            .setTitle(LABELS[action])
            .setMessage(action == 3 ? R.string.phone_end_confirm : R.string.phone_quit_confirm)
            .setNegativeButton(android.R.string.cancel, null)
            .setPositiveButton(LABELS[action], (d, which) -> send(action)).create();
        dialog.show();
    }

    private void showMore() {
        LinearLayout list = new LinearLayout(activity);
        list.setOrientation(LinearLayout.VERTICAL);
        int mask = WesnothActivity.nativeGetPhoneActions();
        for (int id = 6; id < 14; ++id) {
            final int action = id;
            Button entry = button(LABELS[id]);
            entry.setEnabled(mask >= 0 && (mask & (1 << id)) != 0);
            entry.setOnClickListener(v -> {
                dialog.dismiss();
                if (action == 13) confirm(action); else send(action);
            });
            list.addView(entry);
        }
        Button help = button(R.string.phone_help);
        help.setOnClickListener(v -> {
            dialog.dismiss();
            dialog = new AlertDialog.Builder(activity).setTitle(R.string.phone_help)
                .setMessage(R.string.phone_help_text)
                .setPositiveButton(android.R.string.ok, null).create();
            dialog.show();
        });
        list.addView(help);
        android.widget.ScrollView scroll = new android.widget.ScrollView(activity);
        scroll.addView(list);
        dialog = new AlertDialog.Builder(activity).setTitle(R.string.phone_more)
            .setView(scroll).setNegativeButton(android.R.string.cancel, null).create();
        dialog.show();
    }
}
