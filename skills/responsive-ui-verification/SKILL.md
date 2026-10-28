---
name: responsive-ui-verification
description: Verify website or app UI changes with comparable renders and task-state checks across screen sizes, locales and input methods. Use for responsive bugs, visual regressions, preserved-design edits or final UI verification; does not imply a redesign.
---

# Responsive UI Verification

Verify the screen the user will see and the action they need to perform. Source inspection, a successful build, a screenshot and a completed interaction establish different things.

## Establish a comparable baseline

Identify the actual app/worktree, target routes/screens, state, locale and changed components. Read relevant project decisions. Preserve unrelated dirty files. For a content-only edit, record existing composition so a font, theme or layout change does not slip into the task.

Use a reachable preview or the requested live page. A started process is not proof the page responds. Prefer existing lightweight tooling; respect local resource and delegation constraints, serialize heavy checks, and keep only the needed preview server/browser. Enable only a needed local MCP plugin and restore it afterwards if this task enabled it.

For web UI, choose representative widths from the actual layout. A useful initial sample is 390 px mobile and 1440 px desktop; add a narrower width, a tablet or just-around-breakpoint case where risk warrants it. These are samples, not proof of all devices. For native apps, use available platform windows/simulators and distinguish simulator checks from physical-device tests.

Capture before/after using the same route, viewport, locale, content, interaction state and scroll position. Wait for fonts, assets and relevant content to settle. Keep a record of any inspection-only DOM changes; hiding a consent banner can help diagnose an element but cannot count as production overlay verification.

## Check behavior as well as appearance

- **Geometry:** clipped/wrapped headings, real image crop, stable controls, readable density, misplaced overlays and unintended horizontal overflow. Intentional table/gallery scrolling is different from whole-page overflow. Do not “fix” it by hiding overflow without finding the cause.
- **Primary task:** navigation, selection, input, submit, result and recovery relevant to the change. Test actual visible outcomes, not just a click being dispatched.
- **Input and focus:** keyboard order, visible focus, menu/dialog close behavior, escape/back, touch access and no hover-only critical action. Check reduced motion for affected effects.
- **Content stress:** longest supported localized labels, Azerbaijani glyphs, empty lists, missing image/avatar, long product names and realistic data. Do not fabricate live data to obtain a clean screenshot.
- **State stress:** loading, empty, invalid, failed, pending and successful states relevant to the changed flow. Preserve input and avoid duplicate actions under repeated clicks.
- **Shared surfaces:** if a header, token, form primitive or card changed, sample another route that uses it. Do not broaden into a full-site audit without need.

Use DOM measurements for objective questions and rendered images for visual judgement. Scope selectors to the exact component/entity before counting. If a symptom may be browser/OS/tooling-specific, compare a control page or another browser before patching application CSS.

## Close with evidence

Maintain a small matrix: **screen/state → viewport/device → action → expected outcome → observed result → evidence/limit**. Keep failures and untested cases visible. Run repository checks appropriate to changed behavior sequentially. Add an automated regression test when it protects meaningful recurring behavior, not merely a CSS string.

For fixes, resolve reproducible issues within scope and recheck changed cases. For a review, report findings without mutating the app. When a browser/device is unavailable, deliver source-level findings and explicit limits; never claim visual or touch verification from code alone.

For example, a content edit may change wrapping and shift the original composition. Compare the actual renders. Image counts and apparent button counts require exact entity-scoped DOM inspection; a shared browser/OS symptom needs a control comparison before changing application CSS.
