# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.
| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Decimal input "42.7" | "Generate a pytest case that verifies parse_guess handles decimal input by truncating to an int." | `test_parse_guess_handles_decimal` — asserts `parse_guess("42.7")` returns `(True, 42, None)`. | Yes | The parser uses `int(float(raw))` when a period is present, so truncation is the intended behavior. |
| Negative input "-5" | "Generate a pytest case that verifies parse_guess handles negative numbers without crashing." | `test_parse_guess_handles_negative` — asserts `parse_guess("-5")` returns `(True, -5, None)`. | Yes | The game accepts any int; range is enforced at the game level, not in the parser. This proves the parser doesn't reject valid ints. |
| Extremely large int "99999999999999999999" | "Generate a pytest case that verifies parse_guess handles very large integers without overflow." | `test_parse_guess_handles_very_large_number` — asserts the parsed value equals the input. | Yes | Python ints are arbitrary precision, so there's no overflow. This test documents that we rely on that. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

|                          | Model A | Model B |
|--------------------------|---------|---------|
| **Model name**           |         |         |
| **Response summary**     |         |         |
| **More Pythonic?**       |         |         |
| **Clearer explanation?** |         |         |

**Which did you prefer and why?**

<!-- Your conclusion -->
