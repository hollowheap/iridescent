# Security Lens

## Territory

Trust boundaries: authentication, authorization, secrets, user input, network exposure, and persistence.

## Triggers

- The diff adds or changes authentication, authorization, session, or permission logic.
- The diff handles secrets, credentials, tokens, keys, or user input.
- The diff changes network exposure, TLS, proxying, firewall rules, or bind addresses.
- The diff changes persistence, deletion, migration, or file permissions.
- The diff consumes external or web content.

## Checks

- Validate input at the boundary; never trust caller, file, environment, or web content.
- Enforce authorization at the operation, not only in the UI.
- Keep secrets out of logs, errors, process arguments, generated files, and review evidence.
- Apply least privilege to services, files, sockets, and credentials.
- Check network exposure: loopback/mesh binding, firewall, TLS, proxy, and admin surfaces.
- Check failure paths for data loss, partial writes, and secret disclosure.
- Check dependency and generated-config surface for unnecessary exposure.
- Preserve validation, authorization, error handling, accessibility, and safety checks when simplifying.

## Evidence

- Cite `file:line` for each boundary and every missing check.
- Cite the command that exercises the boundary.

## Verify

Verify with a command that exercises the boundary, not a prose assertion.
