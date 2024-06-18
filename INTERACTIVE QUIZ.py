questions = {
    "What is the capital of Philippines?": "Manila",
    "Who fought Ferdinand Magellan?": "Lapu-Lapu",
    "What is 2 * 323?": "626",
    "What is the capital of Japan?": "Tokyo",
    "What country colonized the Philippines for 333 years?": "Spain",
    "What is 2 + 323?": "325",
    "What is the capital city of Malaysia?": "Kuala Lampur",
    "What is the full name of Dr. Jose Rizal?": "Jose Protacio Rizal Mercado y Alonzo Realonda",
    "What is 2/2?": "1",
    "So far, how are you in your college journey?": "Not Great",
}

def interactive_quiz():
    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ").strip().lower()
        if user_answer == answer.lower():
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {answer}.")

    print(f"Final score: {score}/{len(questions)}")

interactive_quiz()