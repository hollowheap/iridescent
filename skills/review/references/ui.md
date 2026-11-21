# UI Lens

## Territory

Rendered interfaces: markup, styles, components, layout, focus, motion, and design tokens.

## Triggers

- The diff changes rendered markup, CSS, components, layout, focus, keyboard behavior, motion, or design tokens.
- The change claims a visual, accessibility, or responsive outcome.
- Supplied screenshots or a rendered report are the only evidence available.

## Checks

- Run a reproducible rendered check from the workspace and cite its command and output.
- Check accessible names, roles, and state (`aria-expanded`, `aria-controls`, `aria-selected`).
- Check visible focus, keyboard order, and activation behavior.
- Check contrast, layout, overflow, and touch targets against the design tokens.
- Check motion and reduced-motion behavior.
- Check that rendered states match the supplied design or brief.

## Evidence

- Cite the probe report path and summary, or the supplied screenshot and `file:line`.
- If no rendered command runs, list every rendered check under `UNVERIFIED` and record the skip reason.

## Verify

Re-run the probe after fixes and compare the report.
