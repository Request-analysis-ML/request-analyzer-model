from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return 'Hello!' 

@app.route('/testing', methods=['POST'])
def test():
    return 'Hello 2!'

@app.route("/favicon.ico")
def favicon():
    return "", 200

if __name__ == '__main__':
    app.run(debug=True ,port=8080,use_reloader=False)