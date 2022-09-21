from live import Live
from utils import get_value_from_user

if __name__ == '__main__':
    live = Live()
    name = get_value_from_user("what is your name?", str)
    print(live.welcome(name))
    live.load_games()
