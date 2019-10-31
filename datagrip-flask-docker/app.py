import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URI')

db = SQLAlchemy(app)


# ----- Home page
@app.route('/')
def homepage_index():
    title = f'Sakila Homepage'
    return render_template('homepage.jinja2', title=title)


# -----  Actors
class Actor(db.Model):
    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))


@app.route('/actors/')
def actors_index():
    title = f'Actors'
    return render_template('actors.jinja2', title=title)


@app.route('/actors/<int:actor_id>')
def actor_index(actor_id):
    actor = Actor.query.filter_by(actor_id=actor_id).first()
    title = f'Actor: {actor.first_name} {actor.last_name}'
    return render_template('actor.jinja2', actor=actor, title=title)
