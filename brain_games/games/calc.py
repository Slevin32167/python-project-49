import operator
import random


def calculate(num1, num2, operation):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

    func = operations[operation]
    return func(num1, num2)


def generate_round():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    correct_answer = str(calculate(num1, num2, operation))
    return question, correct_answer
