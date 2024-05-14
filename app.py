from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def principal():
    return render_template('app.html')

@app.route("/cadastro")
def cadastro():
    return 'Olá sou uma rota de casdastro página de casdastro'

@app.route("/login")
def login():
    return 'realizar Login'

if  __name__ == "__main__":
    app.run(debug=True,Port=6000)