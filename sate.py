from flask import Flask, render_template, url_for
servo1 = 1
servoс = 100
servo2 = 1
servod = 120
servo3 = 1
servov = 150
servo4 = 1
servoh = 150
servo5 = 1
servot = 150
servo6 = 1
servoa = 170
servo7 = 1
servob = 210
servo8 = 1
servow = 220
servo9 = 1
servop = 250


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", servo1=servo1, servoс=servoс, servo2=servo2, servod=servod, servo3=servo3, servov=servov, servo4=servo4, servoh=servoh, servo5=servo5, servot=servot, servo6=servo6, servoa=servoa, servo7=servo7, servob=servob, servo8=servo8, servow=servow,servo9=servo9, servop=servop)


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
    servov += 150
    print(servov)
    print(servo3)
    return ("nothing")

@app.route("/resvard2")
def resvard2():
    global servo3
    global servov
    if servo3 > 1:
        servo3 = servo3-1
        servov -= 150
    print(servov)
    print(servo3)
    return ("nothing")



@app.route('/forvard3')
def forvard3():
    global servoh
    global servo4
    servo4 = servo4+1
    servoh += 150
    print(servoh)
    print(servo4)
    return ("nothing")

@app.route("/resvard3")
def resvard3():
    global servo4
    global servoh
    if servo4 > 1:
        servo4 = servo4-1
        servoh -= 150
    print(servoh)
    print(servo4)
    return ("nothing")


@app.route('/forvard4')
def forvard4():
    global servot
    global servo5
    servo5 = servo5+1
    servot += 150
    print(servot)
    print(servo5)
    return ("nothing")

@app.route("/resvard4")
def resvard4():
    global servo5
    global servot
    if servo5 > 1:
        servo5 = servo5-1
        servot -= 150
    print(servot)
    print(servo5)
    return ("nothing")



@app.route('/forvard5')
def forvard5():
    global servoa
    global servo6
    servo6 = servo6+1
    servoa += 170
    print(servoa)
    print(servo6)
    return ("nothing")

@app.route("/resvard5")
def resvard5():
    global servo6
    global servoa
    if servo6 > 1:
        servo6 = servo6-1
        servoa -= 170
    print(servoa)
    print(servo6)
    return ("nothing")


@app.route('/forvard6')
def forvard6():
    global servob
    global servo7
    servo7 = servo7+1
    servob += 210
    print(servob)
    print(servo7)
    return ("nothing")

@app.route("/resvard6")
def resvard6():
    global servo7
    global servob
    if servo7 > 1:
        servo7 = servo7-1
        servob -= 210
    print(servob)
    print(servo7)
    return ("nothing")


@app.route('/forvard7')
def forvard7():
    global servow
    global servo8
    servo8 = servo8+1
    servow += 220
    print(servow)
    print(servo8)
    return ("nothing")

@app.route("/resvard7")
def resvard7():
    global servo8
    global servow
    if servo8 > 1:
        servo8 = servo8-1
        servow -= 220
    print(servow)
    print(servo8)
    return ("nothing")

@app.route('/forvard8')
def forvard8():
    global servop
    global servo9
    servo9 = servo9+1
    servop += 250
    print(servop)
    print(servo9)
    return ("nothing")

@app.route("/resvard8")
def resvard8():
    global servo9
    global servop
    if servo9 > 1:
        servo9 = servo9-1
        servop -= 250
    print(servop)
    print(servo9)
    return ("nothing")

@app.route('/pasibo')
def pasibo():
    return render_template("pasibo.html")


@app.route('/reg')
def reg():
    return render_template("reg.html")



if __name__ == "__main__":
    app.run("0.0.0.0")
