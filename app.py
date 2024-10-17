from flask import (Flask, render_template, request) # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/<string:nome>", methods=('GET',)) # Assina uma rota
def index(nome): # função responsável pela página
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
    p1 = request.args.get('p1') # use o seu nome
    p2 = request.args.get('p2')
    p3 = request.args.get('p3')
    # HTML retornado
    return f"""<h1>Página inicial</h1>
        <ul><li>{p1}</li><li>{p2}</li><li>{p3}</li></ul>
    """ 

@app.route("/area/<float:largura>/<float:comprimento>", methods=("GET", ))
def area(largura: float, comprimento: float):

    return f"<h1>L={largura}*C={comprimento} -> Área={largura*comprimento}"

@app.route("/parimpar", methods=("GET", ))
def parimpar():
    numero = float(request.args.get("numero"))
    if numero % 2 == 0: 
        return f"<h1>O número {numero} é par!</h1>"
    else:
        return f"<h1>O número {numero} é ímpar!</h1>"

@app.route("/nome", methods=("GET", ))
def nome():
    nome = str(request.args.get("nome"))
    sobrenome = str(request.args.get("sobrenome"))
    return f"<h1>Olá, sr(a) {sobrenome}, {nome}.</h1>"

@app.route("/potencial/<int:numero>/<int:potencia>", methods=("GET", ))
def potencial(numero, potencia):
    return render_template('potencial.html', numero=numero, potencia=potencia)

@app.route("/tabuada/<int:numero>", methods=("GET", ))
def tabuada(numero):
    
    return render_template('tabuada.html', numero=numero)