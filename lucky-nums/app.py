from flask import Flask, request, jsonify, render_template
from models import db, connect_db, User
from forms import AddUserForm
import re, random, requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lucky_number'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_number'

connect_db(app)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route('/api/get-lucky-num', methods=['POST'])
def create_user():
    form = AddUserForm(meta={'csrf': False})

    form.name = request.json['name']
    form.email = request.json['email']
    form.year = request.json['year']
    form.color = request.json['color']

    if not form.validate():
        return (jsonify(errors = form.errors), 201)

    new_user = User(name=form.name, email=form.email,
                    birth_year=form.year, color=form.color, lucky_num=random.randrange(1, 101, 1))
    db.session.add(new_user)
    db.session.commit()

    api_year_response = requests.get(
        f'http://numbersapi.com/{new_user.birth_year}/year?json').json()['text']
    api_num_response = requests.get(
        f'http://numbersapi.com/{new_user.lucky_num}?json').json()['text']
    user_response_json = jsonify(num={'num': f'{new_user.lucky_num}', 'fact': f'{api_num_response}'}, year={'year': f'{new_user.birth_year}', 'fact': f'{api_year_response}'})

    return (user_response_json, 201)