/* SPDX-License-Identifier: GPL-2.0-or-later */
package org.wesnoth.Wesnoth;

import android.app.AlertDialog;
import android.content.SharedPreferences;
import android.content.res.Resources;
import android.graphics.drawable.Drawable;
import android.os.Build;
import android.os.Handler;
import android.os.Looper;
import android.os.SystemClock;
import android.util.TypedValue;
import android.view.Gravity;
import android.view.HapticFeedbackConstants;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.widget.Button;
import android.widget.HorizontalScrollView;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.ScrollView;
import android.widget.Toast;

/**
 * Native-sized touch controls surrounding the SDL game surface.
 *
 * The bar keeps the actions a turn is played with within thumb reach, each with
 * an icon and a short caption; every control also reports its full game action
 * as a content description. Controls the game cannot accept yet are dimmed
 * rather than removed, so the bar never reflows while a unit is selected.
 */
final class PhoneControls {
    // Wire IDs match src/phone_actions.hpp. No dependency on editable hotkeys.
    static final String[] ACTIONS = {
        "cycle", "recruit", "undo", "endturn", "zoomin", "zoomout",
        "objectives", "save", "recall", "unitlist", "leader", "describeunit",
        "preferences", "quit", "moveaction"
    };

    private static final int END_TURN = 3;
    private static final int QUIT = 13;
    private static final int MOVE_ACTION = 14;

    /** Actions on the always-visible bar, in reading order. */
    private static final int[] BAR_ACTIONS = { MOVE_ACTION, 0, 1, 2, 4, 5 };
    /** Actions that only need room once the More sheet is open. */
    private static final int[] SHEET_ACTIONS = { 6, 7, 8, 9, 10, 11, 12, QUIT };

    private static final int[] LABELS = {
        R.string.phone_next, R.string.phone_recruit, R.string.phone_undo,
        R.string.phone_end_turn, R.string.phone_zoom_in, R.string.phone_zoom_out,
        R.string.phone_objectives, R.string.phone_save, R.string.phone_recall,
        R.string.phone_units, R.string.phone_leader, R.string.phone_unit_info,
        R.string.phone_preferences, R.string.phone_quit, R.string.phone_move_action
    };
    /** Short bar captions. Zero keeps the full label, which is already short. */
    private static final int[] SHORT_LABELS = {
        R.string.phone_next_short, R.string.phone_recruit_short, R.string.phone_undo_short,
        R.string.phone_end_turn_short, R.string.phone_zoom_in_short, R.string.phone_zoom_out_short,
        0, 0, 0, 0, 0, 0, 0, 0, 0
    };
    private static final int[] ICONS = {
        R.drawable.phone_ic_next, R.drawable.phone_ic_recruit, R.drawable.phone_ic_undo,
        R.drawable.phone_ic_end_turn, R.drawable.phone_ic_zoom_in, R.drawable.phone_ic_zoom_out,
        R.drawable.phone_ic_objectives, R.drawable.phone_ic_save, R.drawable.phone_ic_recall,
        R.drawable.phone_ic_units, R.drawable.phone_ic_leader, R.drawable.phone_ic_unit_info,
        R.drawable.phone_ic_preferences, R.drawable.phone_ic_quit, R.drawable.phone_ic_move
    };
    private static final int[] VIEW_IDS = {
        R.id.phone_action_cycle, R.id.phone_action_recruit, R.id.phone_action_undo,
        R.id.phone_action_endturn, R.id.phone_action_zoomin, R.id.phone_action_zoomout,
        R.id.phone_action_objectives, R.id.phone_action_save, R.id.phone_action_recall,
        R.id.phone_action_unitlist, R.id.phone_action_leader, R.id.phone_action_describeunit,
        R.id.phone_action_preferences, R.id.phone_action_quit, R.id.phone_action_moveaction
    };

    private static final int POLL_MS = 250;
    private static final int FOCUS_WAIT_MS = 4000;
    /** phone::stale_mask in src/phone_actions.hpp: snapshot too old to trust. */
    private static final int STALE_MASK = -2;
    private static final float CAPTION_SP = 12f;
    private static final float SHEET_CAPTION_SP = 16f;

    private final WesnothActivity activity;
    private final View surface;
    private final LinearLayout bar;
    private final LinearLayout actions;
    private final ImageButton toggle;
    private final Button more;
    private final Button[] buttons = new Button[ACTIONS.length];
    /** More-sheet rows follow the same availability mask as the bar. */
    private final Button[] sheetRows = new Button[SHEET_ACTIONS.length];
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
        bar.setId(R.id.phone_bar);
        bar.setOrientation(LinearLayout.HORIZONTAL);
        bar.setGravity(Gravity.CENTER_VERTICAL);
        bar.setBackgroundResource(R.drawable.phone_bar_background);
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

        toggle = new ImageButton(activity);
        toggle.setId(R.id.phone_bar_toggle);
        toggle.setBackgroundResource(R.drawable.phone_icon_button);
        toggle.setScaleType(ImageView.ScaleType.CENTER_INSIDE);
        toggle.setPadding(dp(12), dp(12), dp(12), dp(12));
        toggle.setMinimumWidth(dp(64));
        toggle.setMinimumHeight(dp(64));
        toggle.setOnClickListener(view -> {
            haptic(view);
            expanded = !expanded;
            settings.edit().putBoolean("expanded", expanded).apply();
            updateLayout(previousMask);
        });
        bar.addView(toggle, new LinearLayout.LayoutParams(dp(64), dp(64)));

        HorizontalScrollView scroll = new HorizontalScrollView(activity);
        scroll.setFillViewport(true);
        scroll.setHorizontalScrollBarEnabled(false);
        actions = new LinearLayout(activity);
        actions.setId(R.id.phone_bar_actions);
        actions.setGravity(Gravity.CENTER_VERTICAL);
        scroll.addView(actions);
        bar.addView(scroll, new LinearLayout.LayoutParams(0,
            ViewGroup.LayoutParams.WRAP_CONTENT, 1));

        for (int id : BAR_ACTIONS) {
            final int action = id;
            boolean primary = action == MOVE_ACTION;
            buttons[action] = barButton(action,
                primary ? R.color.phone_ink : R.color.phone_text_on_button,
                primary ? R.drawable.phone_button_primary : R.drawable.phone_button);
            buttons[action].setOnClickListener(view -> {
                haptic(view);
                send(action);
            });
            actions.addView(buttons[action], actionParams());
        }

        more = barButton(-1, R.color.phone_text_on_button, R.drawable.phone_button);
        more.setId(R.id.phone_action_more);
        more.setText(R.string.phone_more);
        more.setContentDescription(activity.getString(R.string.phone_more));
        setIcon(more, R.drawable.phone_ic_more, R.color.phone_text_on_button);
        more.setOnClickListener(view -> {
            haptic(view);
            showMore();
        });
        bar.addView(more, actionParams());

        buttons[END_TURN] = barButton(END_TURN, R.color.phone_gold,
            R.drawable.phone_button_accent);
        buttons[END_TURN].setOnClickListener(view -> {
            haptic(view);
            confirm(END_TURN);
        });
        bar.addView(buttons[END_TURN], actionParams());

        RelativeLayout.LayoutParams params = new RelativeLayout.LayoutParams(
            ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        params.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM);
        root.addView(bar, params);
        bar.addOnLayoutChangeListener((v, l, t, r, b, ol, ot, or, ob) -> reserveSurface());
    }

    private int dp(int value) {
        return Math.round(value * activity.getResources().getDisplayMetrics().density);
    }

    private void haptic(View view) {
        view.performHapticFeedback(HapticFeedbackConstants.KEYBOARD_TAP);
    }

    private int caption(int action) {
        if (action < 0) return 0;
        int shortLabel = SHORT_LABELS[action];
        return shortLabel != 0 ? shortLabel : LABELS[action];
    }

    private void setIcon(Button view, int icon, int tint) {
        Resources resources = activity.getResources();
        Drawable drawable = resources.getDrawable(icon, activity.getTheme());
        drawable.setTint(activity.getColor(tint));
        int size = dp(18);
        drawable.setBounds(0, 0, size, size);
        view.setCompoundDrawablePadding(dp(6));
        view.setCompoundDrawablesRelative(drawable, null, null, null);
    }

    /** One bar control: at least 48 dp tall and wide, with an icon and a caption. */
    private Button barButton(int action, int textColor, int background) {
        Button view = new Button(activity);
        if (action >= 0) {
            view.setId(VIEW_IDS[action]);
            view.setText(caption(action));
            view.setContentDescription(activity.getString(LABELS[action]));
            setIcon(view, ICONS[action], textColor);
        }
        view.setAllCaps(false);
        view.setTextSize(TypedValue.COMPLEX_UNIT_SP, CAPTION_SP);
        view.setMaxLines(2);
        view.setIncludeFontPadding(false);
        view.setGravity(Gravity.CENTER);
        view.setTextColor(activity.getColor(textColor));
        view.setMinHeight(dp(64));
        view.setMinimumHeight(dp(64));
        view.setMinWidth(dp(64));
        view.setPaddingRelative(dp(10), dp(2), dp(10), dp(2));
        view.setStateListAnimator(null);
        view.setBackgroundResource(background);
        return view;
    }

    private LinearLayout.LayoutParams actionParams() {
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
            ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        params.setMarginStart(dp(4));
        return params;
    }

    /** One More-sheet row: full action name, icon, and a comfortable height. */
    private Button sheetButton(int label, int id, int icon) {
        Button view = new Button(activity);
        view.setId(id);
        view.setText(label);
        view.setContentDescription(activity.getString(label));
        view.setAllCaps(false);
        view.setTextSize(TypedValue.COMPLEX_UNIT_SP, SHEET_CAPTION_SP);
        view.setIncludeFontPadding(false);
        view.setGravity(Gravity.CENTER_VERTICAL | Gravity.START);
        view.setTextColor(activity.getColor(R.color.phone_text));
        setIcon(view, icon, R.color.phone_text);
        view.setMinHeight(dp(72));
        view.setMinimumHeight(dp(72));
        view.setPaddingRelative(dp(16), dp(8), dp(16), dp(8));
        view.setStateListAnimator(null);
        view.setBackgroundResource(R.drawable.phone_sheet_item);
        return view;
    }

    private final Runnable poll = new Runnable() {
        @Override public void run() {
            if (!running) return;
            int mask = WesnothActivity.nativeGetPhoneActions();
            if (mask == STALE_MASK) {
                // No fresh news: keep the controls as the last snapshot left them.
            } else if (mask != previousMask) {
                previousMask = mask;
                for (int i = 0; i < buttons.length; ++i) {
                    if (buttons[i] != null) {
                        boolean enabled = mask >= 0 && (mask & (1 << i)) != 0;
                        buttons[i].setEnabled(enabled);
                        buttons[i].setAlpha(enabled ? 1f : 0.4f);
                    }
                }
                for (Button row : sheetRows) {
                    if (row != null && row.getTag() instanceof Integer) {
                        int action = (Integer) row.getTag();
                        boolean enabled = mask >= 0 && (mask & (1 << action)) != 0;
                        row.setEnabled(enabled);
                        row.setAlpha(enabled ? 1f : 0.4f);
                    }
                }
                updateLayout(mask);
            }
            handler.postDelayed(this, POLL_MS);
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
        dismissDialog();
    }

    private void updateLayout(int mask) {
        bar.setVisibility(mask >= 0 ? View.VISIBLE : View.GONE);
        toggle.setImageResource(expanded ? R.drawable.phone_ic_collapse : R.drawable.phone_ic_expand);
        toggle.setContentDescription(activity.getString(
            expanded ? R.string.phone_hide : R.string.phone_controls));
        ((View) actions.getParent()).setVisibility(expanded ? View.VISIBLE : View.GONE);
        buttons[END_TURN].setVisibility(expanded ? View.VISIBLE : View.GONE);
        more.setVisibility(expanded ? View.VISIBLE : View.GONE);
        RelativeLayout.LayoutParams params = (RelativeLayout.LayoutParams) bar.getLayoutParams();
        params.width = expanded ? ViewGroup.LayoutParams.MATCH_PARENT : ViewGroup.LayoutParams.WRAP_CONTENT;
        params.addRule(RelativeLayout.ALIGN_PARENT_END);
        bar.setLayoutParams(params);
        reserveSurface();
    }

    private void reserveSurface() {
        // A collapsed bar keeps no strip: the toggle floats, so the map gains the space.
        int height = bar.getVisibility() == View.VISIBLE && expanded ? bar.getHeight() : 0;
        if (height == reservedHeight) return;
        reservedHeight = height;
        // SDL receives the resized surface, keeping touch coordinates aligned.
        ViewGroup.MarginLayoutParams params = (ViewGroup.MarginLayoutParams) surface.getLayoutParams();
        params.bottomMargin = height;
        surface.setLayoutParams(params);
    }

    private void send(final int action) {
        final long deadline = SystemClock.uptimeMillis() + FOCUS_WAIT_MS;
        handler.post(new Runnable() {
            @Override public void run() {
                if (!running) return;
                int mask = WesnothActivity.nativeGetPhoneActions();
                // A stale snapshot is not evidence that the action is gone: the
                // player may be confirming a dialog while the game stops
                // publishing. Only a fresh snapshot without the action refuses.
                if (mask != STALE_MASK && (mask < 0 || (mask & (1 << action)) == 0)) {
                    unavailable();
                    return;
                }
                if (activity.hasWindowFocus()
                    && WesnothActivity.nativeQueuePhoneAction(action)) return;
                if (SystemClock.uptimeMillis() < deadline) {
                    handler.postDelayed(this, 50);
                } else {
                    unavailable();
                }
            }
        });
    }

    private void unavailable() {
        Toast.makeText(activity, R.string.phone_unavailable, Toast.LENGTH_SHORT).show();
    }

    private void dismissDialog() {
        if (dialog != null) {
            dialog.dismiss();
            dialog = null;
        }
    }

    private void confirm(int action) {
        dialog = new AlertDialog.Builder(activity)
            .setTitle(LABELS[action])
            .setMessage(action == END_TURN ? R.string.phone_end_confirm : R.string.phone_quit_confirm)
            .setNegativeButton(android.R.string.cancel, null)
            .setPositiveButton(LABELS[action], (d, which) -> {
                dialog = null;
                send(action);
            }).create();
        dialog.show();
    }

    private void showMore() {
        LinearLayout list = new LinearLayout(activity);
        list.setOrientation(LinearLayout.VERTICAL);
        list.setPadding(dp(10), dp(10), dp(10), dp(10));
        int mask = WesnothActivity.nativeGetPhoneActions();
        for (int index = 0; index < SHEET_ACTIONS.length; ++index) {
            final int action = SHEET_ACTIONS[index];
            Button entry = sheetButton(LABELS[action], VIEW_IDS[action], ICONS[action]);
            boolean enabled = mask >= 0 && (mask & (1 << action)) != 0;
            entry.setEnabled(enabled);
            entry.setAlpha(enabled ? 1f : 0.4f);
            entry.setOnClickListener(view -> {
                haptic(view);
                dismissDialog();
                if (action == QUIT) confirm(action); else send(action);
            });
            sheetRows[index] = entry;
            entry.setTag(action);
            list.addView(entry);
        }
        Button help = sheetButton(R.string.phone_help, R.id.phone_action_help, R.drawable.phone_ic_help);
        help.setOnClickListener(view -> {
            haptic(view);
            dismissDialog();
            showHelp();
        });
        list.addView(help);

        ScrollView scroll = new ScrollView(activity);
        scroll.addView(list);
        dialog = new AlertDialog.Builder(activity)
            .setTitle(R.string.phone_more)
            .setView(scroll)
            .setNegativeButton(android.R.string.cancel, null)
            .create();
        dialog.show();
        stretchToScreen(dialog);
    }

    private void showHelp() {
        dialog = new AlertDialog.Builder(activity)
            .setTitle(R.string.phone_help)
            .setMessage(R.string.phone_help_text)
            .setPositiveButton(android.R.string.ok, null)
            .create();
        dialog.show();
    }

    /** Keeps a long list scrollable in landscape instead of running off screen. */
    private void stretchToScreen(AlertDialog target) {
        Window window = target.getWindow();
        if (window == null) return;
        window.setLayout(ViewGroup.LayoutParams.MATCH_PARENT,
            Math.round(activity.getResources().getDisplayMetrics().heightPixels * 0.85f));
    }
}
