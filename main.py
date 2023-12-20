from flask import Flask
from dotenv import load_dotenv
import os
from routes.auth_routes import auth_blueprint
from routes.user_routes import user_blueprint


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.register_blueprint(auth_blueprint, app=app)
app.register_blueprint(user_blueprint)


if __name__ == '__main__':
    app.run(debug=True)