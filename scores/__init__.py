from flask import Flask
from .scores_controller import get_scores

app = Flask(__name__)


@app.route('/')
def scores_server():
    return get_scores()
