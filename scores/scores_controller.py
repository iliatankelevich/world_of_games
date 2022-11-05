from flask import render_template
from .scores import get_current_score


def get_scores():
    try:
        return render_template('./templates/score.html', score=get_current_score())
    except Exception as e:
        return render_template('./templates/error.html', error=str(e))
