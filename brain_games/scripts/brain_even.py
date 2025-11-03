from brain_games.engine import run_game
from brain_games.games import even


def main():
    run_game(even, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == "__main__":
    main()
