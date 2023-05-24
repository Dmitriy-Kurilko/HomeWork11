from utils import *
from flask import Flask, render_template

app = Flask(__name__)


# Список всех кандидатов
@app.route('/')
def print_all_candidates():
    name = load_candidates_from_json()
    return render_template('list.html', name=name)


# Данные о кандидате
@app.route('/candidate/<int:x>')
def print_candidate_by_id(x):
    data = get_candidate_by_id(x)
    return render_template('single.html', data=data)


# Список и кол-во кандидатов по имени
@app.route('/search/<candidate_name>')
def print_candidates_by_name(candidate_name):
    data = get_candidates_by_name(candidate_name)
    return render_template('search.html', data=data)


# Список и кол-во кандидатов по навыкам
@app.route('/skill/<skill_name>')
def print_candidates_by_skill(skill_name):
    data = get_candidates_by_skill(skill_name)
    return render_template('skill.html', data=data, skill_name=skill_name)


app.run()
