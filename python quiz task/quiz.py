#
# ! Start display
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

print(f"\n {format_output}---QUIZ START---{format_reset}")

def quiz_app():
#! Questions and answers
    questions = [
        ("What is the capital of France?", {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"}, "C"),
        ("What is the capital of Japan?", {"A": "Tokyo", "B": "London", "C": "New York", "D": "Rome"}, "A"),
        ("What is the capital of America?", {"A": "Washington D.C", "B": "Berlin", "C": "Los Angeles", "D": "New Orleans"}, "A"),
        ("What is the capital of Canada?", {"A": "Vancouver", "B": "Aurora", "C": "Ottawa", "D": "Toronto"}, "C"),
        ("What is the capital of the UK?", {"A": "Newcastle", "B": "Manchester", "C": "London", "D": "Edinburgh"}, "C"),
    ]

#! Welcome message
    print("\nWelcome! How well do you know your capital cities?")
    print("Please type A, B, C or D for your answer.\n")

    score = 0
#! Display questions and answers
    question_number = 1
    for question, options, correct_answer in questions:
        print(f"Question {question_number}: {question}")
        for option, answer in options.items():
            print(f"{option}: {answer}")
        
#! Take user input and convert to caps for answer and move on if A,B,C or D
#! While loop is necessary to show all answer options
        while True:
            user_answer = input("Your answer: ").upper()
            if user_answer in options:
                break
            else:
                print("Woops. Please type A, B, C, or D.")
#! Correct answer message and add 1 to score
        if user_answer == correct_answer:
            print("That's correct! Great job!\n")
            score += 1
        else:
            print(f"Ahh, unlucky! It's actually {correct_answer}: {options[correct_answer]}\n")
        
        question_number += 1

#! Show them their score out of how many questions and message depending on score
    print(f"Your final score is {score}/{len(questions)}!")
    if score == len(questions):
        print("Great job! Someone's been studying.")
    elif score >= len(questions) // 3:
        print("Not bad, but you could do better!")
    else:
        print("You should probably review your capital cities...")

#! Thank you message
    print("Thank you for taking the quiz!\n")

#! Runs the code
quiz_app()
