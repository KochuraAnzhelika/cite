from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/we')
def we():
    return render_template("we.html")


@app.route('/thenks')
def thenks():
    return render_template("thenks.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "user" + name + "-" + str(id)


if __name__ == "__main__":
    app.run(debug=True)
