from flask import Flask,jsonify, request

app = Flask(__name__)


@app.route('/')
def root():
    return 'hello serch'


if __name__ == '__main__':
    app.run(debug=True)