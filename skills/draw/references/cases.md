# Test Cases

## Ledger Format

# Test Ledger: Sxx

### C01: <behavior>
- Seam: <public seam>
- Type: happy | boundary | failure | provider | consumer | cross-seam
- Setup: <minimum state>
- Action: <observable action>
- Expect: <observable result>
- Red: <exact command and expected failure>
- Covers: <superseded-spec>/<case>   # restoration only

## Coverage

- Happy: one case for the primary observable outcome.
- Boundary: one case for empty, invalid, or limit input.
- Failure: one case for each recorded `Failures:` line.
- Provider: one case proving the seam emits the promised contract.
- Consumer: one case proving a consumer accepts that contract.
- Cross-seam: one case following an outcome through adjacent seams.

## Rules

- Use a unique `Cxx` ID per case.
- Assert the public boundary, never internal calls or private state.
- Record the red command before writing any production code.
- Keep one case focused on one observable behavior per Red command.
