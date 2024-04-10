from flask import Flask
from flask import render_template
from controllers.usuarioController import usuario_blueprint
from models.configDataBase import init_db


app = Flask(__name__)
init_db(app)
#registro de blueprint
app.register_blueprint(usuario_blueprint,url_prefix='/usuario_blueprint')


@app.route('/login')
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password-v2.html')

@app.route('/recover-password')
def recover_password():
    return render_template('recover-password.html')

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/index3',methods=['POST'])
def index3():
    return render_template('index3.html')
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)