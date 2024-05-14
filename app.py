from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def principal():
    titulo = 'O segredo'
    tituloPagina = 'Esse é o subtitulo da página'
    return render_template('app.html', titulo = titulo, tituloPagina = tituloPagina)

@app.route("/cadastro")
def cadastro():
    return 'Olá sou uma rota de casdastro página de casdastro'

@app.route("/login" , methods=['GET', 'POST'])
def login():
    return 'realizar Login'

if  __name__ == "__main__":
    app.run(debug=True)