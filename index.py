# Creator: Adelso Guerra
from flask import Flask, render_template, request
from form import Datos

app = Flask(__name__)

app.secret_key="123456"

# Inicio
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/home')
def home2():
    return render_template("home.html")

# Acerca De
@app.route('/about')
def about():
    return render_template("about.html")

# Noticias
@app.route('/news')
def news():
    return render_template("news.html")

# Ventas
@app.route('/sales')
def sales():
    return render_template("sales.html")

# Entretenimiento
@app.route('/entertainment')
def entertainment():
    return render_template("entertainment.html")

# Formularios 
@app.route('/form1')
def form():
    if request.method=='POST':
        return f"nombre= { request.form['nombre']} | E-mail={ request.form ['correo']} | Telefono={ request.form ['telefono']} "
    return render_template('form1.html')  

@app.route('/form2')
def form2():
    form=Datos()
    if form.validate_on_submit():
        return f"nombre:{ request.form['nombre']} | E-Mail={ request.form['correo']}  |  Teléfono={ request.form['telefono']}"
    return render_template('form2.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
