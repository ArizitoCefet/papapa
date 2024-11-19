from flask import Blueprint, render_template, request, redirect, flash
from models import Cliente
from database import db

bp_cliente = Blueprint('clientes', __name__, template_folder='templates')

@bp_cliente.route('/')
def index():
    dados = Cliente.query.all()
    return render_template('clientes.html', clientes = dados)

@bp_cliente.route('/add')
def add():
    return render_template('clientes_add.html')

@bp_cliente.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    email = request.form.get('email')
    if nome and email:
        bd_cliente = Cliente(nome=nome, email=email)
        db.session.add(bd_cliente)
        db.session.commit()
        flash('Cliente salvo com sucesso!!!')
        return redirect('/clientes')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/clientes/add')
    
@bp_cliente.route("/edita/<int:id>")
def edita(id):
    clientes = Cliente.query.all()
    return render_template("clientes_edita.html", dados=clientes)

@bp_cliente.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    email = request.form.get('email')
    if id and nome and email:
        cliente = Cliente.query.get(id)
        cliente.nome = nome
        cliente.email = email
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/medicamentos')
    else:
        flash('Dados incompletos.')
        return redirect("/medicamentos")





