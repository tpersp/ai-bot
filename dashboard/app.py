from flask import Flask
from dashboard.routes import api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "change_me"

app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
