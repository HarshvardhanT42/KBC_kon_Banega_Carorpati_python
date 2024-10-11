This Python script is a simple quiz game where players answer multiple-choice questions. Each correct answer rewards prize money, and the game ends if the player selects an incorrect answer.

### Key Components:
1. **Questions and Answers:** The script contains a list of three questions, each with four options (A-D) and the correct answer.
2. **Prize Money:** The prizes increase with each question (1000, 5000, and 10000).
3. **Main Game Function:** 
   - The `play_game` function iterates through the questions, displays each one, and asks for the user's answer.
   - If the answer is correct, the player earns prize money. If incorrect, the game ends.
4. **Functions:**
   - `display_question`: Displays the question and its options.
   - `check_answer`: Compares the user's input with the correct answer.
5. **End of Game:** After all questions or an incorrect answer, the total prize is displayed.

### Example Output:
```
What is the capital of France?
A: London
B: Berlin
C: Paris
D: Madrid
Enter your answer (A/B/C/D): C
Correct! You've won 1000 so far. Total prize: 1000
```

This is how the game progresses until the player answers incorrectly or completes all the questions.
