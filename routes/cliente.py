from flask import Blueprint, render_template

cliente_route = Blueprint("cliente", __name__)

""" 
ROTA DE CLIENTES
  
    -/clientes/ (GET) - Listar os clientes

    -/clientes/ (POST) - Inserir o cliente no servidor

    -/clientes/new (GET) - Renderizar o formulario para criar um cliente

    -/clientes/<id> (GET) - Obter os dados de um cliente

    -/clientes/<id>/edit (GET) - Renderizar um formulario para editar um cliente

    -/clientes/<id>/update (PUT) - Atualizar os dados do cliente

    -/clientes/<id>/delete (DELTE) - Deleta o resgistro do usuario

"""

@cliente_route.route('/')
def lista_clientes():
    return {'pagina': 'lista_clientes'}

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    pass

@cliente_route.route('/new')
def form_cliente():
    return {'pagina': 'form_clientes'}

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def autalizar_cliente(cliente_id):
    pass 

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    pass


