from flask import Flask, render_template,request, redirect, url_for
from pyduino import *
#we can import definitions
import time

app= Flask(__name__)

a = Arduino() 
time.sleep(3)
# declare the pins we're using
LED_PIN = 4
ANALOG_PIN = 0

# initialize the digital pin as output
a.set_pin_mode(LED_PIN,'O')
print ("Arduino initialized")

#apis
@app.route('/', methods = ['POST','GET'])
def index():
    # variables for template page (templates/index.html)
    author = "Shubham"
    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':
        # if we press the turn on button
        if request.form['submit'] == 'Turn On': 
            print ("TURN ON")
            # turn on LED on arduino
            #stop automation
            f1= open("xyz.txt", "w")
            f1.write("led")


            f1.close()
            a.digital_write(LED_PIN,1)
            
        # if we press the turn off button
        elif request.form['submit'] == 'Turn Off': 
            print ('TURN OFF')
            
            # turn off LED on arduino
            a.digital_write(LED_PIN,0)

        else:
            pass    
    # read in analog value from photoresistor
    readval = a.analog_read(ANALOG_PIN)
    # the default page to display will be our template with our template variables
    return render_template('index.html', author=author, value=100*(readval/1023.))

@app.route('/manual')
def manual():
    f= open("abc.txt", "w")
    f.write("manual\n")
    f.close()

@app.route('/auto')
def auto():
    f= open("abc.txt", "w")
    f.write("resumed\n")
    f.close()








if __name__ == "__main__":

    app.run(host='0.0.0.0',port=5050)

