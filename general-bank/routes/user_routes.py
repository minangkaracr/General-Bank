from flask import Blueprint
from logic.user_logic import home

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/', methods=['GET'])
def home_route():
    return home()