from flask import Flask,jsonify, request

app = Flask(__name__)


@app.route('/')
def root():
<<<<<<< HEAD
    return 'hello serch1'
=======
    return 'hello serch'
>>>>>>> c98cc9a0a47eddacdd151b08b56c7f97c5ef986c


if __name__ == '__main__':
    app.run(debug=True)