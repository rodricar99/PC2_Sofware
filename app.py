from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys
from sqlalchemy import sql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:melendez2016@localhost:5432/software2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    contraseña = db.Column(db.String(80), nullable=False)


db.create_all()

# LOGEAR USUARIOS


@app.route('/authenticate/login', methods=['POST'])
def authenticate_user():
    error = False
    response = {}
    try:
        username = request.get_json()['username']
        password = request.get_json()['password']
        db.session.query(Usuario).filter(Usuario.nombre == username).filter(
            Usuario.contraseña == password).one()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        response['error_message'] = "Usuario o contraseña incorrecto"
    response['error'] = error
    return jsonify(response)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5003, debug=True)
else:
    print('using global variables from FLASK')
