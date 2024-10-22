from app import app
from flask import render_template, request, redirect, flash, url_for
import pandas as pd

df = pd.DataFrame({
    "Produto": ["Leite", "Queijo", "Maçã", "Carne bovina", "Banana", "Pão", "Tomate", "Ovos", "Arroz"],
    "Categoria": ["Laticínios", "Laticínios", "Frutas", "Carnes", "Frutas", "Panificação", "Hortifrúti", "Alimentos", "Grãos"],
    "Data de Validade": ["2024-12-31", "2024-11-20", "2024-11-15", "2024-11-10", "2024-12-10", "2024-11-25", "2024-11-18", "2024-11-12", "2025-01-15"],
    "Quantidade": ["1 litro", "200g", "5 unidades", "500g", "1 dúzia", "500g", "2kg", "1 cartela", "5kg"]
})

df2 = pd.DataFrame({
    "Nome Cartao": [],
    "Num. Cartao": [],
    "Seg. Cartao": [],
    "Val. Cartao": []
})

@app.route('/')
@app.route('/index')
def index():
    return redirect('/usuario')

@app.route('/geladeira', defaults={"temperatura":10})
@app.route('/geladeira/<int:temperatura>')
def geladeira(temperatura):
    return render_template('geladeira.html', temperatura=temperatura)
    

@app.route('/itens', defaults={"temperatura":10})
@app.route('/itens/<int:temperatura>')
def verItens(temperatura):
    return render_template('geladeira.html', tables=[df.to_html(classes='data')], titles=df.columns.values, tabela=True, temperatura=temperatura)

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
    
@app.route('/salvar-cartao', methods=['POST'])
def salvarCartao():
    cardName = request.form.get('card-name')
    cardNum = request.form.get('card-num')
    cardCode = request.form.get('card-code')
    cardDate = request.form.get('card-date')
    newDf2 = pd.DataFrame({
        "Nome Cartao": [cardName],
        "Num. Cartao": [cardNum],
        "Seg. Cartao": [cardCode],
        "Val. Cartao": [cardDate]
    })
    
    return render_template('usuario.html', tables=[newDf2.to_html(classes='data')], titles=df.columns.values, tabela=True, logado=True)