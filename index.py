from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/news')
def news():
    return render_template("news.html")


@app.route('/ventas')
def ventas():
    return render_template("ventas.html")
# @app.route('/about')
# def about():
#     return "Acerca De"
# @app.route('/news')
# def news():
#     return "Noticias"


if __name__ == '__main__':
    app.run(debug=True)
