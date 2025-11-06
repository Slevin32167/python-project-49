from brain_games.engine import run_game
from brain_games.games import prime


def main():
    run_game(prime, 'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == "__main__":
    main()
