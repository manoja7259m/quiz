import random

with open(r"C:\Users\Admin\Downloads\questions.txt", 'r') as file:
    questions = file.readlines()

with open(r"C:\Users\Admin\Downloads\answers.txt", 'r') as file:
    answers = file.readlines()

num_of_questions = 10

selected_indices = random.sample(range(len(questions)), num_of_questions)
user_score = 0

for i, q_index in enumerate(selected_indices):
    print(f"Question {i + 1}: {questions[q_index]}")
    user_answer = input("Your answer: ").strip().lower()

    correct_answer = answers[q_index].strip().lower()

    if user_answer == correct_answer:
        print("Correct!")
        user_score += 1
    else:
        print(f"Wrong! The correct answer was: {correct_answer}")
    print()

print(f"Quiz Completed! You scored {user_score} out of {num_of_questions}.")