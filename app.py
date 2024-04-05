from flask import Flask, render_template
from dict import recipes

app = Flask (__name__)

@app.route('/')
@app.route('/home')
def home():
    # return 'Hello World'
    return render_template('index.html', recipe_id = 1)

@app.route('/recipes/<int:recipe_number>')
def recipe_list():
    return render_template('recipe_page.html', recipes= recipes)