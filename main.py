from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route

# Inicializacao
app = Flask(__name__)

# Registro de variavel importada 
app.register_blueprint(home_route)

app.register_blueprint(cliente_route, url_prefix='/clientes')



# Execucao
app.run(debug=True)#modo desenvolvedor
