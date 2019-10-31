import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


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
    actors = db.session.execute(text('SELECT * from actor LIMIT 20')).fetchall()
    title = f'Actors'
    return render_template('actors.jinja2', title=title, actors=actors)


@app.route('/actors/<int:actor_id>')
def actor_index(actor_id):
    actors = db.session.execute(text('SELECT * from actor LIMIT 20')).fetchall()
    query_string = 'SELECT * from actor WHERE actor_id = :actor_id'
    query = text(query_string).bindparams(actor_id=actor_id)
    result = db.session.execute(query)
    actor = result.first()
    title = f'Actor: {actor.first_name} {actor.last_name}'
    return render_template('actor.jinja2', actors=actors, actor=actor, title=title)
