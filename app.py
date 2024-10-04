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

@app.route("/area", methods=("GET", ))
def area():
    largura = float(request.args.get("largura"))
    comprimento = float(request.args.get("comprimento"))
    return f"<h1>L={largura}*C={comprimento} -> Área={largura*comprimento}"

@app.route("/potencial/<int:numero>/<int:potencia>", methods=("GET", ))
def potencial(numero, potencia):
    return render_template('potencial.html', numero=numero, potencia=potencia)

@app.route("/tabuada/<int:numero>", methods=("GET", ))
def tabuada(numero):
    
    return render_template('tabuada.html', numero=numero)