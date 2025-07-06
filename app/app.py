from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from app.database.db import DB
from app.routes.test_routes import test_route
from app.routes.user_routes import user_route
from app.routes.products_routes import products_route

load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"/*": {'origins': '*', 'allow_headers': '*', 'methods': '*'}})
DB.init(app)

app.register_blueprint(test_route)
app.register_blueprint(user_route)
app.register_blueprint(products_route)

if __name__ == '__main__':
    app.run(debug=True)