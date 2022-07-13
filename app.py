from email import message
import re
from telnetlib import estatus
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys
from sqlalchemy import sql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:carlitosdion123@localhost:5432/sofware2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ClientePublisher(db.Model):
    __tablename__ = 'cliente_publicador'
    ideaea = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.String(80), nullable=False)
    topic = db.Column(db.String(10), nullable=False)
    estatus=db.Column(db.Boolean, nullable=False)

class ClienteSubscriber(db.Model):
    __tablename__ = 'cliente_subscriptor'
    idea = db.Column(db.Integer, primary_key=True)
    message_view = db.Column(db.String(80), nullable=False)
    topic_view= db.Column(db.String(10), nullable=False)

db.create_all()




@app.route('/Publisher', methods=['POST'])
def authenticate_data():
    error = False
    response = {}
    try:

        comando=request.get_json()[type]
        idea = request.get_json()['idea']
        message = request.get_json()['Message']
        topic = request.get_json()['Topic']
        estatus = request.get_json()['estatus']
        db.session.query(ClientePublisher).filter(ClientePublisher.idea == idea).filter(ClientePublisher.message== message).filter(ClientePublisher.topic == topic).filter(ClientePublisher.estatus == estatus)
        response['type'] = comando

    except FileNotFoundError:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        response['error_message'] = "no existe el usuario"
    response['error'] = error
    return jsonify(response)


@app.route('/subscriber', methods=['GET'])
def response_data():
    error = False
    response = {}
    try:

        comando2=request.get_json()[type]
        idea = request.get_json()['idea']
        message_view = request.get_json()['Message_view']
        topic_view = request.get_json()['Topic_view']
        db.session.query(ClientePublisher).filter(ClienteSubscriber.idea == idea).filter(ClienteSubscriber.message_view== message_view).filter(ClienteSubscriber.topic_view == topic_view)
        response['type'] = comando2

    except FileNotFoundError:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        response['error_message'] = "no existe el usuario"
    response['error'] = error
    return jsonify(response)



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ingresar_data')
def index():
    return render_template('ingresar.html')

if __name__ == '__main__':
    app.run(port=5003, debug=True)
else:
    print('using global variables from FLASK')
