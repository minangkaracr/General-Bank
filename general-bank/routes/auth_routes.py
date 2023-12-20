from flask import Blueprint, request
from logic.auth_logic import register

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register_route():
    return register(request)