from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', nome="Maras")

@app.route('/geladeira')
def geladeira():
    return render_template('geladeira.html')        

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')