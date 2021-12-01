
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

@app.route('/indexBuscando', methods=["POST"])
def indexBuscado():
    documento = request.form["documentoBuscar"]
    clientes=controladorBusqueda.BuscarCliente(documento)
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
    deuda = request.form["saldo"]
    aFavor = 0
    clientes=controladorLista.listando()
    documentos=set([])
    documento=int(documento)
    
    for i in clientes:
        documentos.add(i[0])
    if documento in documentos:
        return redirect(url_for('crearCliente'))
    else:
        documento=str(documento)
        controladorRegistro.RegistrarCliente(documento, nombre, movil, direccion, deuda, aFavor)
        return redirect(url_for('index'))

@app.route('/modificarCliente')
def modificarCliente():
    return render_template('modificarC.html')

@app.route('/modificandoCliente', methods=["POST"])
def modificandoCliente():
    documento = request.form["documentoBuscar"]
    cliente=controladorBusqueda.BuscarCliente2(documento)
    return render_template('modificandoCliente.html',cliente=cliente, documento=documento)

@app.route('/clienteModificado',methods=["POST"])
def clienteModificado():
    documento = request.form["documento"]
    direccion = request.form["direccion"]
    movil = request.form["numero_cel"]
    cliente=controladorActualizar.actualizarCliente(documento,movil,direccion)
    return redirect(url_for('index'))
    

@app.route('/actualizarCuenta')
def modificaDeuda():
    return render_template('modificarD.html')

@app.route('/modificandoDeuda', methods=["POST"])
def modificandoDeuda():
    documento= request.form["documentoBuscar"]
    cliente=controladorBusqueda.BuscarCliente3(documento)
    return render_template('modificandoDeuda.html', cliente=cliente, documento=documento)

@app.route('/actualizandoDeuda', methods=["POST"])
def actualizandoDeuda():
    if request.method == 'POST':
        monto =int(request.form['montoIng'])
        documento = request.form['documento']
        
        if request.form.get('Deuda') == 'Deuda':
            
            aFavor=controladorSaldo.aFavor(documento)
            aFavorActual=int(aFavor[0])
            
            if aFavorActual==0:
                deuda=(controladorSaldo.Deuda(documento))
                deudaActual=int(deuda[0])
                deudaActual=deudaActual+monto
                controladorSaldo.CambiarDeuda(deudaActual, documento)
                cliente=controladorBusqueda.BuscarCliente3(documento)
                return render_template('modificandoDeuda.html', cliente=cliente, documento=documento)

            elif aFavorActual>0:
                deuda=(controladorSaldo.Deuda(documento))
                deudaActual=int(deuda[0])
                resultado=aFavorActual-monto
                
                if resultado<0:
                    deudaActual=resultado*(-1)
                    aFavorActual=0
                    cliente=controladorSaldo.CambiarDeuda(deudaActual,documento)
                    cliente=controladorSaldo.CambiarAFavor(aFavorActual, documento)
                    cliente=controladorBusqueda.BuscarCliente3(documento)
                    return render_template('modificandoDeuda.html', cliente=cliente, documento=documento)
                
                elif resultado>=0:
                    aFavorActual=resultado
                    deudaActual=0
                    cliente=controladorSaldo.CambiarDeuda(deudaActual,documento)
                    cliente=controladorSaldo.CambiarAFavor(aFavorActual, documento)
                    cliente=controladorBusqueda.BuscarCliente3(documento)
                    return render_template('modificandoDeuda.html', cliente=cliente, documento=documento)
                
        elif request.form.get('A Favor') == 'A Favor':
            
            deuda=controladorSaldo.Deuda(documento)
            deudaActual=int(deuda[0])
            
            if deudaActual>0:
                deudaActual=deudaActual-monto
                
                if deudaActual<0:
                    aFavor=deudaActual*(-1)
                    deudaActual=0
                    cliente=controladorSaldo.CambiarAFavor(aFavor,documento)
                    cliente=controladorSaldo.CambiarDeuda(deudaActual,documento)
                    cliente=controladorBusqueda.BuscarCliente3(documento)
                    return render_template('modificandoDeuda.html', cliente=cliente, documento=documento)
                
                elif deudaActual>0:
                    cliente=controladorSaldo.CambiarDeuda(deudaActual,documento)
                    cliente=controladorBusqueda.BuscarCliente3(documento)
                    return render_template('modificandoDeuda.html', cliente=cliente, documento=documento)
                
                else:
                    cliente=controladorSaldo.CambiarDeuda(deudaActual,documento)
                    cliente=controladorBusqueda.BuscarCliente3(documento)
                    return render_template('modificandoDeuda.html', cliente=cliente, documento=documento)
    
                    
if __name__=='__main__':
    app.run(debug=True, port=7000)
