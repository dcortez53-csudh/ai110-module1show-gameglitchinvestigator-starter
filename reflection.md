# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- Answer: The first time I ran the game it loaded cleanly in the browser with a Streamlit interface: a sidebar with a difficulty selector, a main panel for guessing, and a "Developer Debug Info" expander. Nothing crashed, but the behavior was clearly wrong, the hints contradicted the outcomes, the range text didn't match the selected difficulty, and the "Attempts left" counter was already reduced before I'd made a single guess.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
- Answer: The three bugs I noticed first were: (1) the hint messages were flipped, after a "Too High" outcome the hint said "Go HIGHER!"; (2) the info text always said "1 to 100" and "New Game" always picked from 1-100, ignoring the selected difficulty, and (3) the attempts counter started inconsistently between a fresh load and a "New Game" click, which threw off the displayed attempts-let and the score

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|make a guess higher than the secret |outcome "Too High" and hint "Go LOWER!"|outcome "Too High" but hint reads" Go HIGHER!" (messages are flipped).|none |
|select a difficulty (e.g., Hard)|displayed range and new secret use the difficulty's range (e.g., Hard = 1-50).|sidebar shows correct range, but info text says "1 to 100" and New Game picks randint (1,100) ignoring difficulty.|none|
|start a game and submit guesses|the UI shows full attempts remaining until the first submit; first submit increments attempts to 1 and scoring reflects attempt #1|"Attempts left" counter is already reduced before any guess, and the displayed score changes that follow don't match the visible attempt count|none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Answer: I used GitHub Copilot's chat panel inside PyCharm. I attached app.py and logic_utils.py as context and asked Copilot to help summarize and explain where I noticed any bugs, walking through the specific lines of code causing each bug.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Answer: Copilot's diagnosis of the hint-reversal bug. I asked it to explain why a guess above the scret returned a "Go HIGHER!" hint, and it pointed to 'check_guess' in 'appy.py' (lines ~36-47), where the branches for 'guess > secret' and 'guess < secret' return the correct outcome ("Too High"/"Too Low") but swap the mesages ("Go HIGHER!"/"Go LOWER!"). I verified this by opening the function, tracing the two branches by hand, and confirming that the outcome strings were correct while the emoji messages were inverted.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
- Answer: Copilot line numbers are approximate, there would be a suggestion for a particular line of code, and the file itself would have a different number. I re-read the whole 'check_guess' function and the submit handler to locate the bugs myself then used Copilot only to confirm the logic rather than the line numbers. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
