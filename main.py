
from werkzeug.utils import redirect
from controladores import controladorRegistro, controladorBusqueda, controladorActualizar, controladorSaldo, controladorLista
from flask import Flask, render_template, request, url_for

app=Flask(__name__)
app.secret_key= 'my_secret_key'
@app.route('/')
@app.route('/index')
def index():
    clientes=controladorLista.listando()
    return render_template('index.html',clientes=clientes)

@app.route('/crearCliente')
def crearCliente():
    return render_template('crearC.html')

@app.route('/creandoCliente', methods=["POST"])
def creandoCliente():
    nombre = request.form["nombreCliente"]
    documento = request.form["numeroDoc"]
    direccion = request.form["direccion"]
    movil = request.form["numeroCel"]
    saldo = request.form["saldo"]
    clientes=controladorLista.listando()
    documentos=set([])
    print (clientes)
    documento=int(documento)
    
    for i in clientes:
        documentos.add(i[0])
        print (documentos)
    if documento in documentos:
        return redirect(url_for('crearCliente'))
    else:
        documento=str(documento)
        controladorRegistro.RegistrarCliente(documento, nombre, movil, direccion, saldo)
        return redirect(url_for('index'))

@app.route('/modificarCliente')
def modificarCliente():
    return render_template('modificarC.html')

@app.route('/actualizarCuenta')
def modificaDeuda():
    return render_template('modificarD.html')


if __name__=='__main__':
    app.run(debug=True, port=7000)
