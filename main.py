from flask import Flask
from controllers.usuarioController import usuario_blueprint
from configDataBase import init_db

app = Flask(__name__)
init_db(app)
#registro de blueprint
app.register_blueprint(usuario_blueprint)

if __name__ == '__main__':
    app.run()