from flask import Blueprint, render_template, request, redirect, flash
from models import Pedido, Cliente
from database import db

bp_pedido = Blueprint('pedidos', __name__, template_folder='templates')

@bp_pedido.route('/')
def index():
    dados = Pedido.query.all()
    return render_template('pedido.html', pedidos = dados)

@bp_pedido.route('/add')
def add():
    c = Cliente.query.all()
    return render_template('pedido_add.html', clientes = c)

@bp_pedido.route('/save', methods=['POST'])
def save():
    id_cliente = request.form.get('id_cliente')
    valor_total = request.form.get('valor_total')
    data = request.form.get('data')
    if id_cliente and valor_total and data:
        bd_pedido = Pedido(id_cliente, valor_total, data)
        db.session.add(bd_pedido)
        db.session.commit()
        flash('Pedido salvo com sucesso!!!')
        return redirect('/pedidos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/pedidos/add')





