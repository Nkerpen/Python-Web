## pip install flask
## pip install -U Flask-SQLAlchemy

## Importar o servidor de HTML e de Renderização
from flask import Flask
from controllers import routes
from models.database import db
import os

## Define os metadados 
# um nome para o projeto e dizer aonde encontrá-lo, que no caso, é a pasta views
app = Flask(__name__,template_folder="views")

#Permite ler um path (caminho do SO)
basedir =os.path.abspath(os.path.dirname(__file__))

#Caminho do banco
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "models/estudantes.sqlite3")

## Função para iniciar a aplicação
routes.init_app(app)

##  Roda o projeto
if __name__ == "__main__":
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)
    