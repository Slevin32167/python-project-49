import random

MIN_NUMBER = 1
MAX_NUMBER = 50


def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    correct_answer = str(find_gcd(num1, num2))
    question = f"{num1} {num2}"
    return question, correct_answer
