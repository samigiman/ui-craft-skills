---
name: ui-deslop
description: Audit or remove generic AI-looking patterns from an existing website or app while preserving its brand and working flows. Use for requests such as AI slop təmizlə, UX/UI trashdan qurtar, or make this interface less generic; review requests remain read-only.
---

# UI Deslop

Replace generic decisions with product-specific ones. “AI slop” describes a weak outcome here; it does not prove how the interface was made. A gradient, font, framework, icon library, card or rounded corner alone is not a defect.

## Inspect before editing

Read the current brief and relevant project instructions. Locate the actual app/worktree, rendered target, shared components and styles. Capture the current state where possible. Record what must be preserved: brand assets, useful density, requested interactions, content and functioning controls.

Use the user's verb to choose the mode: “bax/yoxla/analiz et” means inspect and report; “təmizlə/düzəlt” authorizes scoped fixes. Historical instructions are evidence, not new authorization. Existing project choices take priority over this skill's preferences.

For a large codebase, optionally run `python3 scripts/scan_ui_candidates.py PATH`. It only finds source patterns for inspection. Read [references/patterns.md](references/patterns.md) to interpret them. Neither the script nor keyword frequency can establish design quality.

## Identify the real problems

Inspect clusters of symptoms with a visible consequence:

- **Generic structure:** the same hero, badge, card grid and vague CTA could describe any company; key product content sits below filler.
- **Competing emphasis:** everything has a glow, border, icon or oversized label, so the user cannot locate the next action.
- **Decorative overload:** particles, cursor followers, repeated orbit diagrams, dotted backgrounds or entry effects consume attention without explaining anything.
- **Hollow proof:** invented stats, clients, reviews, photos or an apparent integration that has no working path.
- **Weak content and states:** vague copy, duplicate actions, ambiguous stock or price, unclear errors, loading that looks like success, or a placeholder presented as finished UI.
- **Incoherent execution:** unrelated image styles, mismatched crops, inconsistent type hierarchy, arbitrary radii, clipped translations or mobile overlays covering the task.

For each finding, record the exact screen/state, evidence, effect on the task, and replacement. Distinguish a reproduced failure from an aesthetic judgement. Prioritize the problems that prevent understanding or completion.

## Repair the smallest coherent surface

1. Restore hierarchy and content first: useful headings, visible real values, explicit actions, appropriate grouping and sensible density.
2. Replace the layout primitive where necessary. Removing a shadow from a poor card grid does not fix the structure; deleting content to make it empty does not fix it either.
3. Reduce decoration selectively. Keep intentional brand color, requested imagery, useful motion and a chosen visual metaphor. Do not impose an all-white, all-black, editorial or brutalist replacement everywhere.
4. Remove the effect's implementation as well as its paint when the effect is no longer needed: canvas loops, event listeners, timers, observers and imports. If only CSS can be changed, document that limit. A hidden animation may still use CPU.
5. Edit component/source styles coherently. Avoid accumulating global `!important` overrides, suppressing all headings, hiding required controls or masking overflow to conceal a broken layout. A scoped legacy override can be pragmatic when source is unavailable.
6. Preserve functioning behavior. Do not rewrite auth, payments, data, tracking or external destinations merely to improve visual polish.

## Verify the repair

Compare before/after at the same route, viewport, content and state. Check the primary flow, keyboard focus, touch access, long localized text, loading/empty/error/success states and reduced motion where relevant. Ensure removed effects stop running and no longer leave empty space.

For fixes, deliver the changed UI plus concise evidence and remaining limits. For reviews, report the highest-impact findings with specific replacements. Do not invent a “slop score” or call a technical build pass a visual acceptance.
