from flask import Blueprint, render_template

indexRoute = Blueprint('index', __name__)

@indexRoute.route('/', methods=["GET", "POST"])
def index():
    return render_template('pages/index.html')