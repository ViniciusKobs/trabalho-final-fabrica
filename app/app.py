from flask import Flask

from app.database.db import DB
from app.routes.test_routes import test_route
from app.routes.user_routes import user_route

app = Flask(__name__)
DB.init(app)

app.register_blueprint(test_route)
app.register_blueprint(user_route)

if __name__ == '__main__':
    app.run(debug=True)