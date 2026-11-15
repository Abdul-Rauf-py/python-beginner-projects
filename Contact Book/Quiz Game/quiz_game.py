import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Go", "Gd", "Au", "Ag"],
        "answer": "Au"
    }
]


def the_game():
    score=0
    random.shuffle(questions)
    for position_of_question,question in enumerate(questions,start=1):
        print(f"{position_of_question}. {question["question"]}")
        for position_of_options,options in enumerate(question['options'],start=1):
            print(f'{position_of_options}. {options}')
        answer_of_player = input("Enter your answer: ")
        if answer_of_player.lower() == question["answer"].lower():
            print("You are correct!")
            score+=1
        else:
            print("You are wrong!")

    print(f"Your total score is: {score}")

print('''
            WELCOME!
Are you ready for a fun quiz game?
            yes/no
''')
choice_to_play = input("enter your choice(yes/no): ")
if choice_to_play.lower() == 'yes':
    the_game()
elif choice_to_play.lower() == 'no':
    print("You can play when you like it there is no rush about it.")
else:
    print("Only choose yes or no.")

