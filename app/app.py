from flask import Flask

from app.controllers.TestController import TestController
from app.http.dispatcher import dispatch

app = Flask(__name__)

@app.route('/test', methods=["GET", "POST"])
def __test():
    return dispatch(TestController.index)

if __name__ == '__main__':
    app.run(debug=True)
