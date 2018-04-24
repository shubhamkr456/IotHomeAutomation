import RPi.GPIO as GPIO
from flask import Flask, render_template
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#setup for gpio pins
b_1=4
b_2=17
b_3=27
b_4=22
b_5=5
b_6=6
b_7=13
b_8=19
#NOW THE STATUS OF INPUT PINS
b0 =GPIO.LOW
b1 =GPIO.LOW
b2 =GPIO.LOW
b3 =GPIO.LOW
b4 =GPIO.LOW
b5 =GPIO.LOW
b6 =GPIO.LOW
b7 =GPIO.LOW
#intializing inputs
GPIO.setup(b_1, GPIO.IN)
GPIO.setup(b_2, GPIO.IN)
GPIO.setup(b_3, GPIO.IN)
GPIO.setup(b_4, GPIO.IN)
GPIO.setup(b_5, GPIO.IN)
GPIO.setup(b_6, GPIO.IN)
GPIO.setup(b_7, GPIO.IN)
GPIO.setup(b_8, GPIO.IN)

@app.route("/")
def index():
    #reading status of each pin and deciding
    b7=GPIO.input(b_8)
    time.sleep(0.001)
    b7=GPIO.input(b_8)
    
    b6=GPIO.input(b_7)
    time.sleep(0.001)
    b6=GPIO.input(b_7)

    b5=GPIO.input(b_6)
    time.sleep(0.001)
    b5=GPIO.input(b_6)

    b4=GPIO.input(b_5)
    time.sleep(0.001)
    b4=GPIO.input(b_5)

    b3=GPIO.input(b_4)
    time.sleep(0.001)
    b3=GPIO.input(b_4)

    b2=GPIO.input(b_3)
    time.sleep(0.001)
    b2=GPIO.input(b_3)

    b1=GPIO.input(b_2)
    time.sleep(0.001)
    b1=GPIO.input(b_2)

    b0=GPIO.input(b_4)
    time.sleep(0.001)
    b0=GPIO.input(b_4)

    #clearing the inputs!! is remaining

    x = (1*b0)+(2*b1)
    x = x+(4*b2)+(8*b3)
    x = x+(16*b4)+(32*b5)
    x = x+(64*b6)+(128*b7)

    b0 =GPIO.LOW
    b1 =GPIO.LOW
    b2 =GPIO.LOW
    b3 =GPIO.LOW
    b4 =GPIO.LOW
    b5 =GPIO.LOW
    b6 =GPIO.LOW
    b7 =GPIO.LOW

    time.sleep(1)
    current=x*0.078125
    voltage=current*330
    powerdissipated=current*voltage
    
    templateData = {
        'title' : 'Project Title',
        'current'  : current,
        'power'  : powerdissipated,
        'voltage' : voltage
           }
    return render_template('index.html', **templateData)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7050, debug=True)






