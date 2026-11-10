# UI Lens

## Territory

Rendered interfaces: markup, styles, components, layout, focus, motion, and design tokens.

## Triggers

- The diff changes rendered markup, CSS, components, layout, focus, keyboard behavior, motion, or design tokens.
- The change claims a visual, accessibility, or responsive outcome.
- Supplied screenshots or a rendered report are the only evidence available.

## Checks

- When `opal` is active, run `~/.opal/bin/ui-probe audit <url>` and `~/.opal/bin/ui-probe source .`; cite the report summary.
- Check accessible names, roles, and state (`aria-expanded`, `aria-controls`, `aria-selected`).
- Check visible focus, keyboard order, and activation behavior.
- Check contrast, layout, overflow, and touch targets against the design tokens.
- Check motion and reduced-motion behavior.
- Check that rendered states match the supplied design or brief.

## Evidence

- Cite the probe report path and summary, or the supplied screenshot and `file:line`.
- List every check that could not run under unverified.

## Verify

Re-run the probe after fixes and compare the report.

## Skip

Skip when the diff reaches no rendered surface, or when `opal` is not invoked. List rendered checks under unverified.
