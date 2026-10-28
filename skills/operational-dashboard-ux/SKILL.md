---
name: operational-dashboard-ux
description: Design or refine task dashboards, admin panels and agent workspaces for clear filtering, dense readable work and truthful status. Use when operators cannot find a date/segment, understand progress, edit safely or distinguish real work from a visual demo.
---

# Operational Dashboard UX

Make the next operational decision clear. An admin panel is a working surface, not a landing page full of decorative metric cards.

## Understand the operator's job

Inspect the actual screen, data shape, controls, role permissions, domain language and main repeated task. Identify the entity, time range, segment and action the operator needs. Preserve existing useful behavior and deliberate visual identity; a pixel-art office can remain playful while presenting precise work states.

Separate review from implementation according to the request. Use fixtures or read-only records for verification; UI work does not authorize live customer messages, paid model calls, orders, campaign changes or publishing.

## Build around useful information

- Keep active date range, account/project and filters visible. Support the requested granularity: day, selected date span or segment. A month selector is insufficient when the operator needs two particular days.
- Show what a metric means, its unit, source and freshness where they affect the decision. Preserve legitimate source distinctions such as sales, credit contracts, enquiries and ad-platform results. Unknown is not zero; demo values are not live results.
- Use a compact work list or table when scanning, sorting and comparing records is the job. Use cards where entities or summaries genuinely warrant them. Prioritize values and exceptions over decorative icons.
- Use stable alignment, tabular numerals for comparable numbers, readable labels and useful color-coded state with text. Do not replace legibility with extreme low contrast or make every status a bright pill.
- Place search, filters and consequential actions near the records they affect. Distinguish row selection from navigation; keep bulk-action scope explicit. Existing authorization rules still apply.
- For repeated edits, preserve scroll, filter and selection context; use an appropriate inline editor or detail drawer. Save state should reflect persisted results and validation errors should preserve input.
- On mobile, identify essential columns and provide accessible detail/actions. A deliberately scrollable data region can be appropriate; a clipped whole page cannot.

## Represent work truthfully

Derive status from actual task/provider/result state. Make these distinctions wherever relevant: queued, running, waiting, blocked, failed, cancelled and completed; installed, signed in, connected and tested; draft, saved and published.

Do not animate agents “working” when nothing is running, show simulated progress as measured progress, or call a configured provider callable without a verified request. Provide a visible reason and next action for blocked work. Keep provenance, useful timestamps, cancellation and resumable context aligned with supported behavior. Avoid filling the product screen with implementation internals that do not help the operator decide.

## Validate an operational cycle

Exercise the actual requested filter/date change, record open/edit path, validation failure and save/result state in a safe environment. Check loading, empty, stale, partial-error and cancelled states that the workflow supports. Confirm totals and visible filters describe the same subset. For status-only work, a screenshot of a green badge is insufficient; compare it to the underlying state.

Preserve the main data distinctions while simplifying presentation. Deliver the improved decision/task path and evidence. Do not expand a dashboard request into an unrelated reporting-platform migration.

## Worked examples

- A dashboard with only a month selector cannot satisfy a request to compare two selected days. Verify the range, records and totals together.
- A technically validated data tool can still miss the requested screen redesign. Show the real task surface and workflow, not only test counts.
- A deliberately playful agent workspace can retain its visual metaphor while distinguishing waiting, blocked and tested-provider states. Do not substitute simulated work for observable progress.
