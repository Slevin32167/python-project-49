import random


def generate_progression(start, step, length):
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))
    return progression


def generate_round():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)

    progression_list = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression_list[hidden_index]

    progression_list[hidden_index] = '..'
    question = " ".join(progression_list)

    return question, correct_answer
