from flask.wrappers import Request
from controladores import controladorRegistro, controladorBusqueda, controladorActualizar, controladorSaldo
from flask import Flask, render_template

app=Flask(__name__)
app.secret_key= 'my_secret_key'
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/crearCliente')
def crearCliente():
    return render_template('crearC.html')

@app.route('/creandoCliente')
def creandoCliente():
    nombre=Request.form['nombre']
    return render_template('index.html')

@app.route('/modificarCliente')
def modificarCliente():
    return render_template('modificarC.html')

@app.route('/actualizarCuenta')
def modificaDeuda():
    return render_template('modificarD.html')


if __name__=='__main__':
    app.run(debug=True, port=7000)
