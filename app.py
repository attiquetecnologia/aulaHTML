from flask import (Flask, request) # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota
def index(): # função responsável pela página
    nome = request.args.get('nome') # use o seu nome
    # HTML retornado
    return f"""<h1>Página inicial</h1>
        <p>Olá {nome}, que nome bonito!
    """ 

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>Contato</h1>"

@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>Galeria</h1>"

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre</h1>"

@app.route("/personagens", methods=('GET',)) # Assina uma rota
def personagens(): # função responsável pela página
    p1 = 'Goku' # use o seu nome
    p2 = "Mega-Man"
    p3 = "Super Patos"
    # HTML retornado
    return f"""<h1>Página inicial</h1>
        <ul><li>{p1}</li><li>{p2}</li><li>{p3}</li></ul>
    """ 