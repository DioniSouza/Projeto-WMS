from flask import Blueprint,request, jsonify
from.models import Produto
from . import db

bp =Blueprint('produtos',__name__)

@bp.route('/produtos',methods=['POST'])

def criar_produto():
    dados = request.get_json()
    produto = Produto(
        nome=dados['nome'],
        descricao=dados.get('descricao'),
        codigo_barras=dados['codigo_barras'],
        validade=dados.get('validade'),
        quantidade=dados.get('quantidade', 0)
    )
    db.session.add(produto)
    db.session.commit()
    return jsonify({"id": produto.id, "nome": produto.nome}), 201