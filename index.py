# Creator: Adelso Guerra
from flask import Flask, render_template

app = Flask(__name__)

#Inicio
@app.route('/')
def home():
    return render_template("home.html")

#Acerca De
@app.route('/about')
def about():
    return render_template("about.html")

#Noticias
@app.route('/news')
def news():
    return render_template("news.html")

#Ventas
@app.route('/sales')
def sales():
    return render_template("sales.html")

#Entretenimiento
@app.route('/entertainment')
def entertainment():
    return render_template("entertainment.html")

# if __name__ == '__main__':
#     app.run(debug=True)
