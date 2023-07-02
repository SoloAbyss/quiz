"""This is a Te Reo Maori Quiz."""

import random
import time
import os


def delete_multiple_lines():
    """Clear the console output."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def countdown(c, time_limit):
    """Countdown timer when starting quiz."""
    while c >= 0:
        if c > 0:
            print(f"{c}...", end="\n")
        else:
            print("GO!")
        time.sleep(1)
        c -= 1


def ask_question(question):
    """Asks the questions."""
    print(question["question"])
    for i, answer in enumerate(question["answers"]):
        print(f"{i+1}. {answer}")

    valid_answers = [str(i + 1) for i in range(len(question["answers"]))]

    while True:
        user_answer = input("Enter the number of your answer: ")
        if user_answer in valid_answers:
            break
        else:
            print(
                "Sorry, that's not a valid option."
                "Please choose an answer from 1 to 4.\n"
            )

    user_answer = int(user_answer)

    if user_answer == question["correct_answer"] + 1:
        delete_multiple_lines()
        print("Correct!\n")
        return 1
    else:
        correct_index = question["correct_answer"]
        correct_answer = question["answers"][correct_index]
        delete_multiple_lines()
        print("Incorrect! The correct answer was:", correct_answer, "\n")
        return 0


def play_quiz(questions, hard_mode=False):
    """Play the quiz."""
    score = 0
    total_questions = len(questions)
    time_limit = 15 if hard_mode else 0
    start_time = time.time()

    for question in questions:
        score += ask_question(question)

        if time_limit > 0 and time.time() - start_time >= time_limit:
            delete_multiple_lines()
            print("Times Up!")
            break

    if time_limit == 0 or time.time() - start_time < time_limit:
        print("Quiz finished! Your score:", score, "/", total_questions)

    while True:
        play_again = input("Would you like to play again? (Yes/No): ").lower()
        if play_again == "yes":
            delete_multiple_lines()
            return True
        elif play_again == "no":
            delete_multiple_lines()
            return False
        else:
            print("Hmm, that doesn't seem right. Only type in YES or NO.")


def quiz_start():
    """Start the quiz."""
    questions_fruit = [
        {
            "question": "What is the Maori word for APPLE?",
            "answers": ["Āporo", "Wharepaku",
                        "Pākihi", "Kōtirotiro"],
            "correct_answer": 0,
        },
        {
            "question": "What is the Maori word for ORANGE?",
            "answers": ["Ārani", "Kōwhitiwhiti",
                        "Karāti", "Tīhi"],
            "correct_answer": 0,
        },
        {
            "question": "What is the Maori word for PEACH?",
            "answers": ["Wharepēke", "Kōraka",
                        "Pītiti", "Pūteketeke"],
            "correct_answer": 2,
        },
        {
            "question": "What is the Maori word for LEMON?",
            "answers": ["Kōremu", "Rēmana",
                        "Wharepure", "Pūtangitangi"],
            "correct_answer": 1,
        },
        {
            "question": "What is the Maori word for WATERMELON?",
            "answers": ["Pūmate", "Wharemērēti",
                        "Kōmerenika", "Merengi"],
            "correct_answer": 3,
        },
        {
            "question": "What is the Maori word for PLUM?",
            "answers": ["Wharepēke", "Kōraka",
                        "Paramu", "Pūteketeke"],
            "correct_answer": 2,
        },
        {
            "question": "What is the Maori word for GRAPES?",
            "answers": ["Kerepe", "Kōraka",
                        "Pītiti", "Pūteketeke"],
            "correct_answer": 0,
        },
    ]

    questions_veggies = [
        {
            "question": "What is the Maori word for CORN?",
            "answers": ["Pukarākau", "Kānga",
                        "Whakangāka", "Pōhākai"],
            "correct_answer": 1,
        },
        {
            "question": "What is the Maori word for ONION?",
            "answers": ["Wairuku", "Pāhukura",
                        "Whakarāhui", "Aniana"],
            "correct_answer": 3,
        },
        {
            "question": "What is the Maori word for CABBAGE?",
            "answers": ["Kāpeti", "Pōhakuwhero",
                        "Whakamauī", "Kōhutukawa"],
            "correct_answer": 0,
        },
        {
            "question": "What is the Maori word for CAULIFLOWER?",
            "answers": ["Kareparāoa", "Whakanuihuka",
                        "Pōhakahukarere", "Kōhurere"],
            "correct_answer": 0,
        },
        {
            "question": "What is the Maori word for CARROT?",
            "answers": ["Whakamārama", "Pōharakoa",
                        "Kāreti", "Kōhutau"],
            "correct_answer": 2,
        },
        {
            "question": "What is the Maori word for CUCUMBER?",
            "answers": ["Kōhuhina", "Pōhapara",
                        "Whakaninihā", "Kūkama"],
            "correct_answer": 3,
        },
        {
            "question": "What is the Maori word for LETTUCE?",
            "answers": ["Kōhutaka", "Rētihi",
                        "Whakatakataka", "Pōharua"],
            "correct_answer": 1,
        },
        {
            "question": "What is the Maori word for POTATO?",
            "answers": ["Rīwai", "Whakanoho",
                        "Kōhununu", "Pōharore"],
            "correct_answer": 0,
        },
    ]

    questions_gen_items = [
        {
            "question": "What is the Maori word for TV?",
            "answers": [
                "Pātakaarata",
                "Pouaka Whakaata",
                "Whakamāharahara",
                "Hītoriwhakaāhua",
            ],
            "correct_answer": 1,
        },
        {
            "question": "What is the Maori word for COFFEE TABLE?",
            "answers": ["Rākaukawhe", "Papara Kawhe",
                        "Kōrerorangi", "Whakararaenga"],
            "correct_answer": 1,
        },
        {
            "question": "What is the Maori word for BED?",
            "answers": ["Whakararoturuma", "Moemoeāroha",
                        "Whakapōtiki", "Moenga"],
            "correct_answer": 3,
        },
        {
            "question": "What is the Maori word for DRAWERS?",
            "answers": ["Whakararanga", "Pūtātara",
                        "Toroa", "Whakapātaka"],
            "correct_answer": 2,
        },
        {
            "question": "What is the Maori word for SMARTPHONE?",
            "answers": ["Waea Atamai", "Tamahiko",
                        "Pātikaranga", "Kōreromahi"],
            "correct_answer": 0,
        },
        {
            "question": "What is the Maori word for TOASTER?",
            "answers": ["Tahuwhakarihi", "Whakatōhi",
                        "Kōreropūhoro", "Pūrahatete"],
            "correct_answer": 1,
        },
        {
            "question": "What is the Maori word for OVEN?",
            "answers": ["Pōkaiwhakaara", "Tīwaiwera",
                        "Whakararotu", "Umu"],
            "correct_answer": 3,
        },
    ]

    random.shuffle(questions_fruit)
    random.shuffle(questions_veggies)
    random.shuffle(questions_gen_items)

    hard_mode_time_limit = 15

    while True:
        print(
            "Kia ora! Welcome to the Māori Language Quiz."
            "Please choose a category to test "
            "your Te Reo Māori knowledge:\n\n"
            "1. Fruits\n"
            "2. Vegetables\n"
            "3. General Items\n"
        )

        category_choice = input("Enter the number of your chosen category: ")

        if category_choice == "1":
            delete_multiple_lines()
            difficulty = input(
                "Choose difficulty level: \n\n"
                "1. Easy (no time limit)\n"
                "2. Hard (15 second time limit)\n\n"
                "Select what difficulty you want: "
            ).lower()
            delete_multiple_lines()
            countdown(3, hard_mode_time_limit if difficulty == "2" else 0)
            if difficulty == "2":
                play_again = play_quiz(questions_fruit, hard_mode=True)
            else:
                play_again = play_quiz(questions_fruit)
        elif category_choice == "2":
            delete_multiple_lines()
            difficulty = input(
                "Choose difficulty level: \n\n"
                "1. Easy (no time limit)\n"
                "2. Hard (15 second time limit)\n\n"
                "Select what difficulty you want: "
            ).lower()
            delete_multiple_lines()
            countdown(3, hard_mode_time_limit if difficulty == "2" else 0)
            if difficulty == "2":
                play_again = play_quiz(questions_veggies, hard_mode=True)
            else:
                play_again = play_quiz(questions_veggies)
        elif category_choice == "3":
            delete_multiple_lines()
            difficulty = input(
                "Choose difficulty level: \n\n"
                "1. Easy (no time limit)\n"
                "2. Hard (15 second time limit)\n\n"
                "Select what difficulty you want: "
            ).lower()
            delete_multiple_lines()
            countdown(3, hard_mode_time_limit if difficulty == "2" else 0)
            if difficulty == "2":
                play_again = play_quiz(questions_gen_items, hard_mode=True)
            else:
                play_again = play_quiz(questions_gen_items)
        else:
            print("That doesn't seem right.")
            continue

        if not play_again:
            break

    print("\nThank you for playing the Māori Language Quiz. Ka kite anō!\n")


quiz_start()
