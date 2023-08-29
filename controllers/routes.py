from flask import render_template, request, url_for, redirect
from models.database import db,Estudante

##rota para que a página seja aberta
def init_app(app):
    @app.route("/")

    # def sempre utilizada para determinar Funções
    def index():

        # Atribuindo valores para variaveis no GET
        # escola = "ETEC"
        # cidade = "Registro"
        # escola2 = "Ana Pinto"
        
        estudantes = Estudante.query.all()
        
        # renderizar a página escolhida
        return render_template("index.html",
                               # Resgatando os valores no GET
                            #    pEscola=escola, 
                            #    pCidade=cidade,
                            #    pEscola2=escola2
                            
                            pEstudantes=estudantes
                            
                            )

    # @app.route("/crud")
    # def crud():
    #     return render_template("crud.html")
    
    # @app.route("/T")
    # def macaco():
    #     return render_template("verdeterre.html")