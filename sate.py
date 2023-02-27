from flask import Flask, render_template, url_for
servo1 = 1
servoс = 100
servo2 = 1
servod = 120
servo3 = 1
servov = 150
servo4 = 1
servoh = 150


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", servo1=servo1, servoс=servoс, servo2=servo2, servod=servod, servo3=servo3, servov=servov)


@app.route('/forvard')
def forvard():
    global servoс
    global servo1
    servo1 = servo1+1
    servoс += 100
    print(servoс)
    print(servo1)
    return ("nothing")


@app.route("/resvard")
def resvard():
    global servo1
    global servoс
    if servo1 > 1:
        servo1 = servo1-1
        servoс -= 100
    print(servoс)
    print(servo1)
    return ("nothing")






@app.route('/forvard1')
def forvard1():
    global servod
    global servo2
    servo2 = servo2+1
    servod += 120
    print(servod)
    print(servo2)
    return ("nothing")

@app.route("/resvard1")
def resvard1():
    global servo2
    global servod
    if servo2 > 1:
        servo2 = servo2-1
        servod -= 120
    print(servod)
    print(servo2)
    return ("nothing")





@app.route('/forvard2')
def forvard2():
    global servov
    global servo3
    servo3 = servo3+1
    servov += 120
    print(servov)
    print(servo3)
    return ("nothing")

@app.route("/resvard2")
def resvard2():
    global servo3
    global servov
    if servo3 > 1:
        servo3 = servo3-1
        servov -= 120
    print(servov)
    print(servo3)
    return ("nothing")









@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/we')
def we():
    return render_template("we.html")


@app.route('/thenks')
def thenks():
    return render_template("thenks.html")


if __name__ == "__main__":
    app.run(debug=True)
