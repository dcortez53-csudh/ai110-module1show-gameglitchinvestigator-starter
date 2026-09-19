# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"?
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** Move the logic into `logic_utils.py` and run `pytest`.

## 📝 Document Your Experience

The game is a Streamlit number-guessing app. The player selects a difficulty,
gets a secret number in a range, and submits guesses. After each guess, the
game shows a hint ("Go HIGHER!" / "Go LOWER!") and updates the score. The
player wins by guessing the secret within the attempt limit.

### Bugs found

1. **Hint messages were reversed.** A guess that was too high returned the
   outcome "Too High" but the hint "Go HIGHER!" — exactly backwards. The
   same was true for a too-low guess.
2. **Difficulty range was ignored.** The sidebar showed the correct range
   for each difficulty, but the info text always said "1 to 100" and the
   "New Game" button always picked a secret from 1–100, regardless of the
   selected difficulty.
3. **Attempt counter was inconsistent.** On a fresh load the counter started
   at 1, but "New Game" reset it to 0. This made the "Attempts left" display
   wrong before the first guess and threw off the Win points formula.

### Fixes applied

- Refactored `get_range_for_difficulty`, `parse_guess`, `check_guess`, and
  `update_score` out of `app.py` into `logic_utils.py`.
- Corrected the hint messages in `check_guess` so "Too High" says "Go LOWER!"
  and "Too Low" says "Go HIGHER!".
- Replaced the hardcoded `1 and 100` in the info text and `randint(1, 100)`
  in New Game with the `low` and `high` values from
  `get_range_for_difficulty`.
- Initialized `st.session_state.attempts` to `0` so the first submit becomes
  attempt 1 and the "Attempts left" display is accurate.
- Removed the `secret = str(...)` flip in the submit handler that forced the
  comparison into a buggy string-comparison path on even attempts.
- Adjusted the Win points formula from `100 - 10 * (attempt_number + 1)` to
  `100 - 10 * attempt_number`.

## 📸 Demo Walkthrough

1. User opens the app. Sidebar shows Difficulty = Normal, Range = 1 to 100,
   Attempts allowed = 8.
2. User enters a guess of 40 in the text box and clicks "Submit Guess 🚀".
3. Game returns hint "📈 Go HIGHER!" and updates attempts to 1. Attempts
   left now shows 7.
4. User enters a guess of 70 and submits. Game returns "📉 Go LOWER!".
   Attempts is now 2.
5. User narrows the range with more guesses; the hints consistently tell
   them which direction to move.
6. User enters the correct secret. Game shows "🎉 Correct!", balloons
   appear, status becomes "won", and the final score is displayed.
7. Clicking "New Game 🔁" resets attempts to 0, picks a fresh secret within
   the current difficulty range, and clears the score and history.

## 🧪 Test Results

============================= test session starts =============================
platform linux -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
collected 10 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 10%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 20%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 30%]
tests/test_game_logic.py::test_parse_guess_handles_empty PASSED          [ 40%]
tests/test_game_logic.py::test_parse_guess_handles_non_number PASSED     [ 50%]
tests/test_game_logic.py::test_parse_guess_accepts_int PASSED            [ 60%]
tests/test_game_logic.py::test_range_for_easy PASSED                     [ 70%]
tests/test_game_logic.py::test_range_for_hard PASSED                     [ 80%]
tests/test_game_logic.py::test_update_score_win_decreases_with_attempts PASSED [ 90%]
tests/test_game_logic.py::test_update_score_too_low_loses_points PASSED  [100%]

============================== 10 passed in 0.05s ==============================

## 🚀 Stretch Features

- [ ] Not attempted.