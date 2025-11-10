def run_game(game_module, description):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)

    correct_answers_needed = 3

    for _ in range(correct_answers_needed):
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").lower()

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. ", end="")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
