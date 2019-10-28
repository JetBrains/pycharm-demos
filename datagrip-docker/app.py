import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URI')

db = SQLAlchemy(app)


class Actor(db.Model):
    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))


@app.route('/actors/<int:actor_id>')
def index(actor_id):
    actor = Actor.query.filter_by(actor_id=actor_id).first()
    return f'<h1>Hello {actor.first_name}</h1>'
