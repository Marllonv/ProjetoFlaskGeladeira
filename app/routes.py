from app import app
from flask import render_template, request, redirect, flash
import pandas as pd

df = pd.DataFrame({
    "Produto": ["Leite", "Queijo", "Maçã", "Carne bovina"],
    "Categoria": ["Laticínios", "Laticínios", "Frutas", "Carnes"],
    "Data de Validade": ["2024-12-31", "2024-11-20", "2024-11-15", "2024-11-10"],
    "Quantidade": ["1 litro", "200g", "5 unidades", "500g"]
})

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', nome="Maras")

@app.route('/geladeira')
def geladeira():
    return render_template('geladeira.html')
        
@app.route('/itens')
def verItens():
    return render_template('geladeira.html',  tables=[df.to_html(classes='data')], titles=df.columns.values, tabela=True)

@app.route('/usuario')
def usuario():
    return render_template('usuario.html', logado=False)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario == 'admin' and senha=='admin':
        return render_template('usuario.html', logado=True)
    else:
        flash("Dados Inválidos")
        return redirect('/usuario')

