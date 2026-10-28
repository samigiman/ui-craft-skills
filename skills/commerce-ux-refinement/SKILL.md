---
name: commerce-ux-refinement
description: Improve storefront product discovery, variants, purchase actions, cart, registration and account UX. Use for confusing commerce flows, unclear stock/delivery/price, generic profile UI or a shopping interface that looks polished but is hard to use.
---

# Commerce UX Refinement

Help the customer identify the right product, understand the offer and complete the next step. Preserve exact product/variant identity and current business rules.

## Trace the real path

Inspect the current catalog/search, product detail and relevant purchase or account path. Use exact route, product ID, variant and locale; similar titles and image URLs can refer to different products. Review requests remain read-only; fix requests authorize the stated UI changes, not unrelated catalog writes or purchases.

Find the concrete friction: discovery, choice, confidence, input or feedback. Distinguish a UI failure from missing business data or a backend problem. Use real content or clearly scoped fixtures; keep sample-data results separate from live integration claims.

## Product discovery and choice

- Make search, categories and useful filters easy to reach. On mobile, expose active filters and a clear reset; preserve the user's place after opening a product and going back.
- Present coherent product cards: correct image, understandable title, meaningful differences, actual price and stock, with an unmistakable action. Do not make every badge equally prominent.
- Keep imagery stable as content changes. Inspect the actual rendered asset, crop, duplicates, model and color. Counting URL strings does not establish a useful unique gallery.
- Group true variants as choices in the existing product model. Display the selected color/RAM/storage and update image, availability, price and destination coherently. Preserve scroll/context where appropriate; do not turn a cosmetic fix into an unrequested catalog migration.
- Avoid competing purchase actions with ambiguous outcomes. Verify the DOM before counting controls: a title and subtitle inside one button are not two actions.

## Offer and purchase states

Explain actual cash price, valid discounts, installment terms and delivery where available. Never invent a free-delivery benefit, crossed-out price, financing plan or warranty. Unsupported commercial details need correct data, not attractive filler.

Keep unavailable items and actions intelligible according to the business rule. An out-of-stock notification action should look actionable if it works; the purchase action should communicate its actual availability. Use words as well as color. Preserve any requested public visibility rule.

For cart and checkout, preserve entered data on validation failures, show the specific correction, avoid duplicate submissions and distinguish pending, failed and completed outcomes. Reflect server-confirmed totals and stock. Verify with a non-purchasing test path or authorized fixtures; this skill does not authorize a real order or message.

## Registration and account

Separate sign in, create account and password recovery clearly. Collect only fields needed for the actual flow. Keep labels persistent, show the error next to its cause, preserve safe input and return focus predictably.

When a signed-in user has a valid profile image, show it in the account entry point with a suitable fallback if it fails. Keep order history, profile, addresses and support discoverable; do not turn account screens into a marketing page.

For localized sites, verify navigation, role/job labels, form labels, validation, product attributes and account states in the selected language. Preserve product names and units where appropriate. Localized copy must fit the layout and make the same promise.

## Verify the changed path

Exercise representative available/unavailable, guest/signed-in, selected-variant and validation states relevant to the change. Check narrow mobile, desktop, keyboard and back navigation. A desktop screenshot cannot prove a mobile keyboard or native touch interaction.

Report the corrected friction, changed screen and observed outcome. Read [references/design-examples.md](references/design-examples.md) for product identity, delivery wording and account examples.
