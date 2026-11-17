# Interrogation Protocol

Use for every brainstorm that is not a clear one-line task.

## Design Tree

- Write the destination, hard constraints, and known facts before asking.
- Model each unresolved decision as a node; its dependent decisions are branches.
- The frontier is every node whose prerequisites are settled.
- Find facts in the repository, tools, and primary sources.
- Ask the user only for preferences, goals, risk tolerance, and scope.
- Never ask for a fact that the request or repository already answers.

## Rounds

1. Call the host's structured question tool; never ask unresolved questions as plain chat text.
2. Ask only frontier questions in one call; defer dependent questions to a later round.
3. Give each question 2-4 concrete options, one recommended answer, and one line stating what each answer changes.
4. Use `multi: true` only when selections are independent; otherwise ask one decision per question.
5. Recompute the frontier after each answer and repeat until empty.
6. Say when an assumption becomes a default and invite correction.

## Stop

- Stop when the frontier is empty and you can predict the user's reaction to the next three questions.
- Restate destination, user, why now, success, binding constraint, and out of scope in the user's words.
- Ask "What is wrong or missing?" and require explicit approval before recording the recommendation or moving to `design`.
- If answers stay generic, ask "If you did not have to justify this to anyone, what would you actually want?"
- Block when a fork changes what gets built and only the user can decide it.
