from flask import Blueprint, request, current_app
from logic.auth_logic import register, login

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register_route():
    return register(request)

@auth_blueprint.route('/login', methods=['POST'])
def login_route():
    return login(request, current_app)