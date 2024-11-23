from flask import Flask, render_template, request
app = Flask(__name__)

#Exemplo GET

@app.route('/')
def inicio():
    # Renderiza a página inicial com o formulário
    return render_template('inicio.html')

@app.route('/filme', methods=['GET'])
def filme():
    #Obtém o valor enviado pelo campo do formulário que possui o atributo name="filmefav"
    filme = request.args.get('filmefavorito') 
    return render_template('filme.html', filme=filme)


#Exemplo POST

@app.route('/retangulo')
def retangulo():
    return render_template('retangulo.html')

@app.route('/calcularetangulo',methods=["POST"])
def calcularetangulo():
    lado1 = int(request.form.get('lado1'))
    lado2 = int(request.form.get('lado2'))
    perimentro = 2*(lado1+lado2)
    area = lado1*lado2
    return render_template('calcularetangulo.html',resultperimetro=perimentro, resultarea=area)