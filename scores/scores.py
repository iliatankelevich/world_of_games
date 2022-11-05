from utils import SCORES_FILE_NAME


def add_score(difficulty: int):
    file = None
    try:
        current_score = get_current_score()
        current_score_int = 0 if current_score is None else int(current_score)
        new_score = current_score_int + (difficulty * 3) + 5
        file = open(SCORES_FILE_NAME, 'w')
        file.write(str(new_score))
    finally:
        if file is not None:
            file.close()


def get_current_score() -> int:
    file = None
    try:
        file = open(SCORES_FILE_NAME, 'r')
        current_score = file.readline()
        return int(current_score)
    except FileNotFoundError as e:
        print('no score file found')
    finally:
        if file is not None:
            file.close()
