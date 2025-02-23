from flask import Flask, url_for, render_template

# Inicializacao
app = Flask(__name__)

# rotas
@app.route('/')
def ola_mundo():
    titulo = "Gestao de Usuarios"
    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "Mario", "membro_ativo": False},
        {"nome": "Maria", "membro_ativo": True}
    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)

@app.route('/oi')
def oi():
    return "ola, mundo"


# execucao
app.run(debug=True)#modo desenvolvedor
