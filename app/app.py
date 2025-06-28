from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/helloworld', methods=["GET", "POST"])
def hello_world():
    response = {
        "message": "Hello World!"
    }
    return jsonify(response)


@app.route('/start', methods=["GET", "POST"])
def start():
    response = {
        "message": "start!"
    }
    return jsonify(response)











if __name__ == '__main__':
    app.run()
