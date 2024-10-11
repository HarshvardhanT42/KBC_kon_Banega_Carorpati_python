import sys

# List of questions, options and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A: London", "B: Berlin", "C: Paris", "D: Madrid"],
        "answer": "C"
    },
    {
        "question": "What is the highest mountain in the world?",
        "options": ["A: K2", "B: Kangchenjunga", "C: Lhotse", "D: Everest"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A: Harper Lee", "B: Mark Twain", "C: J.K. Rowling", "D: Ernest Hemingway"],
        "answer": "A"
    }
]

# Prize money for each question
prizes = [1000, 5000, 10000]

# Function to display a question
def display_question(q, options):
    print("\n" + q)
    for option in options:
        print(option)

# Function to check the answer
def check_answer(user_answer, correct_answer):
    return user_answer.upper() == correct_answer

# Main game function
def play_game():
    total_prize = 0
    for i, q in enumerate(questions):
        display_question(q["question"], q["options"])
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        
        if check_answer(user_answer, q["answer"]):
            total_prize += prizes[i]
            print(f"Correct! You've won {prizes[i]} so far. Total prize: {total_prize}")
        else:
            print("Incorrect answer. Game over.")
            break

    print(f"You're taking home a total of {total_prize}!")

# Run the game
if __name__ == "__main__":
    play_game()
