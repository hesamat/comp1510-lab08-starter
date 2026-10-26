PLAYS_PATH = "plays.txt"
SCORES_PATH = "scores.json"


def parse_play(line):
    raise NotImplementedError


def read_plays(path):
    raise NotImplementedError


def save_scores(scores, path):
    raise NotImplementedError


def load_scores(path):
    raise NotImplementedError


def top_scores(scores, count):
    raise NotImplementedError


def plays_by_game(scores):
    raise NotImplementedError


def main():
    """
    Print the Ridge Arcade board report.
    """
    print("=== The Ridge Arcade ===")


if __name__ == "__main__":
    main()
