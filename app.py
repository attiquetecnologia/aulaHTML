from flask import (Flask, render_template, request, url_for) # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/")
@app.route("/<string:nome>", methods=('GET',)) # Assina uma rota
def index(nome=None): # função responsável pela página
    # HTML retornado
    return render_template('index.html')

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

@app.route("/parimpar/<float:numero>", methods=("GET", ))
def parimpar(numero):
    if numero % 2 == 0: 
        return f"<h1>O número {numero} é par!</h1>"
    else:
        return f"<h1>O número {numero} é ímpar!</h1>"

@app.route("/nome/<string:nome>/<string:sobrenome>", methods=("GET", ))
def nome(nome, sobrenome):
    return f"<h1>Olá, sr(a) {sobrenome}, {nome}.</h1>"

@app.route("/potencial/<int:numero>/<int:potencia>", methods=("GET", ))
def potencial(numero, potencia):
    return render_template('potencial.html', numero=numero, potencia=potencia)

@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET", ))
def tabuada(numero = None): # None desobriga o valor
    
    if 'numero' in request.args: # se argumento existir
        numero = request.args.get('numero') # atualiza numero

    return render_template('tabuada.html', numero=numero)

@app.route("/calculo_juros")
def calculo_joros():
    total = 0
    if 'meses' in request.args:
        investimento = float(request.args.get('investimento_inicial'))
        juros = float(request.args.get('juros'))
        aporte = float(request.args.get('aporte'))
        meses = float(request.args.get('meses'))
        total = (investimento+aporte*meses)*juros/100

    return render_template('calculo_juros.html', total=total)