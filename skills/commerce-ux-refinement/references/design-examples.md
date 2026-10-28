# Commerce examples

| Symptom | Inspect | Correction to verify |
| --- | --- | --- |
| Color choices appear to be unrelated products | Variant model, route, selected state and assets | Coherent product identity, visible selection and appropriate context retention |
| RAM switching feels like leaving the product | Loading behavior, URL, scroll and back navigation | Clear updated variant state, correct image/price/stock |
| Profile icon ignores an available user photo | Signed-in state, image source and failure fallback | Real avatar where available, usable fallback otherwise |
| Registration screen is visually crowded | Sign-in, registration, recovery and validation paths | One clear task per state with persistent useful input |
| Removing “free delivery” still implies a free service | Text, icon, price label and neighboring cues | The full rendered offer reflects the actual delivery rule |
| Gallery image count looks implausible | Exact product scope and rendered media | Inspect actual unique model/color images, not URL count alone |
| Multiple apparent purchase labels | DOM button boundaries and actual outcomes | Distinct outcomes are understandable; a subtitle is not counted as a second button |
| Language changes only update navigation | Role labels, forms, validation and attributes | The full relevant flow follows the selected locale |

Do not fix presentation ambiguity by inventing a financing plan, warranty, discount or stock value. Preserve the business rule and use an authorized non-purchasing verification path.
