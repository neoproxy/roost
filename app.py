#!flask/bin/python
from flask import Flask, render_template
import random
from data import Articles
from dice import DiceResults
from jsonnpctest import nonpc

app = Flask(__name__)

Articles = Articles()
DiceResults = DiceResults()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/npc')
def npc():
    return render_template('npc.html',  data=nonpc())

@app.route('/traps')
def traps():
    return render_template('traps.html')

@app.route('/tavern')
def tavern():
    return render_template('tavern.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/articles/<string:id>/')
def article(id):
    return render_template('article.html', id = id)

if __name__ == '__main__':
    app.run(debug=True)
