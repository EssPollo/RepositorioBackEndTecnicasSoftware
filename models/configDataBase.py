from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Qq.789456@localhost/CES' #mONGODB, SQLite, Sq
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)