# Design Examples

## Bad
- Requirement states a design choice: `- [ ] R01: Add a custom hide flag.`
- Open decision recorded as `- [ ] D01` instead of blocking with the question tool.

## Good
- [ ] R01: Closing the app keeps background sync running while the window is hidden.
  - Verify: close the window and check the tray process remains active.
  - Acceptance: Sync continues without a visible window.
  - Constraints: none.
  - Non-goals: start at login.

### Module Seams

- [x] D01 [R01]: Reuse the desktop tray option.
  - Context: Background sync needs a hidden window; the desktop already owns tray state.
  - Alternatives: custom window flag, daemon process.
  - Consequences: inherits the desktop tray toggle and its lifecycle.
