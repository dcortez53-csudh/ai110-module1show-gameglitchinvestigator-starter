| Input                               | Expected Behavior                                                                                                                   | Actual Behavior                                                                                                                                 | Console Output / Error |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| Make a guess higher than the secret | Outcome "Too High" and hint "Go LOWER!"                                                                                             | Outcome "Too High" but hint reads "Go HIGHER!" (messages are flipped).                                                                          | none                   |
| Select a difficulty (e.g., Hard)    | Displayed range and new secret use the difficulty's range (e.g., Hard = 1–50).                                                      | Sidebar shows correct range, but info text says "1 to 100" and New Game picks randint(1, 100) ignoring difficulty.                              | none                   |
| Start a game and submit guesses     | The UI shows full attempts remaining until the first submit; first submit increments attempts to 1 and scoring reflects attempt #1. | "Attempts left" counter is already reduced before any guess, and the displayed score changes that follow don't match the visible attempt count. | none                   |


## 2. How did you use AI as a teammate?

I used GitHub Copilot's chat panel inside PyCharm for this project. I attached `app.py` and `logic_utils.py` as context so the AI could see both the UI layer and the logic layer at once.

One correct AI suggestion: when I asked Copilot to explain why a guess above the secret returned "Go HIGHER!", it correctly traced the bug to the `if / else` block in `check_guess`. It pointed out that the *outcome* strings ("Too High" / "Too Low") were right, but the *hint messages* underneath them were swapped. I verified this by reading the function myself and by writing a pytest case (`test_guess_too_high`) that asserts the hint contains "LOWER".

One AI suggestion I did not accept as written: Copilot's first pass at `update_score` kept the `attempt_number + 1` term in the Win formula, which is the source of the off-by-one bug. I rejected that and used `100 - 10 * attempt_number` instead, because `attempts` already starts at 0 and increments by 1 before scoring, so adding 1 again double-counts the attempt. I verified with `test_update_score_win_decreases_with_attempts`, which confirms a first-attempt win scores higher than a fifth-attempt win.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed when both the pytest suite passed and the app behaved correctly in the browser. After refactoring into `logic_utils.py` I ran `python -m pytest tests/ -v` and all 10 tests passed. Then I ran the app and confirmed the four key behaviors: Hard shows "Range: 1 to 50", New Game picks a secret inside that range, a too-high guess says "Go LOWER!", and the "Attempts left" counter reads 8 before the first guess on Normal.

One test that was especially useful was `test_guess_too_high`. It directly targets the original hint-reversal bug: it calls `check_guess(60, 50)` and asserts that the returned outcome is `"Too High"` and the message contains `"LOWER"`. That single test would have caught the bug in the original code.

Copilot helped me design tests by suggesting the naming convention (`test_guess_too_high`, `test_range_for_easy`, etc.) and pointing out that I should test the tuple-return form of `check_guess` rather than the old single-string form. I reviewed each suggestion and adjusted the assertions where needed.

---

## 4. What did you learn about Streamlit and state?

Streamlit re-runs the entire Python script from top to bottom every time a user interacts with the page — clicking a button, typing in a text box, changing a dropdown. That is called a "rerun." A plain Python variable would be reset to its initial value on every rerun, so it cannot remember anything between clicks. `st.session_state` is a dictionary that survives reruns. Anything stored there — like the secret number, the attempt counter, or the score — persists across interactions. The original buggy code stored `attempts` as `1` at first load and `0` on New Game, which is why the "Attempts left" counter was already reduced before the first guess.

---

## 5. Looking ahead: your developer habits

One habit or strategy from this project that I want to reuse: asking the AI to explain *why* a bug exists before asking it to fix it. When Copilot walked me through `check_guess` step by step, I understood the root cause instead of just accepting a patch. I want to keep that "explain first, then fix" pattern.

One thing I would do differently next time: I would take a screenshot or write down the exact buggy behavior before asking the AI anything. A few times I had to describe the bug from memory, which made my prompts less precise and led to one wrong suggestion from the AI.

How this project changed the way I think about AI-generated code: AI-generated code can look clean and even claim to be "production-ready" while having subtle logic bugs that only surface at runtime. I now treat generated code as a first draft that needs to be tested, not a finished product.