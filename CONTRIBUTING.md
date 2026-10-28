# Contributing

Useful contributions change a decision, improve a real workflow or prevent a demonstrated failure.

1. Describe the actual UI problem and the request the skill should handle.
2. Use a small public or synthetic example. Remove private client data, credentials and conversation exports.
3. Keep the change focused. Preserve the user's chosen product, brand, scope and authorization.
4. Add a reference only when it provides useful conditional detail. Avoid blanket bans on colors, fonts, components or motion.
5. Run structural validation and the relevant tests:

   ```bash
   python3 -m pip install -r requirements-dev.txt
   python3 scripts/validate.py
   python3 -m unittest discover -s tests -v
   ```

For a design claim, include the route/state, viewport, observed effect and a proposed replacement. If you tested an agent on a real prompt, distinguish its actual output from your expected behavior and document what could not be verified.

Do not add runtime dependencies, automatic publishing, external messaging or a mandatory approval ritual to an ordinary styling task without a concrete reason. Keep skill descriptions precise enough that unrelated tasks do not load them.

By contributing, you agree to make your contribution available under the repository's MIT license.
