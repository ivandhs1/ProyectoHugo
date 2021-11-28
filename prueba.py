from flask import Flask, render_template

app=Flask(__name__)
app.secret_key = 'my_secret_key'
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/crear_cliente')
def crearCliente():
    return render_template('crearC.html')

if __name__=='__main__':
    app.run(debug=True, port=7000)
