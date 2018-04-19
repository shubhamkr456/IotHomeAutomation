from pyduino import *
#from definitions import *
from temperature import *
import time

if __name__ == '__main__' :
    print("Establishing connection with Arduino")
    a= Arduino()
    time.sleep(3)
    print ("Established connection with arduino")

    #pins Setup
    led_pin = 4
    water_pump=2
    soil= 5 
    pir= 7

    # initiate the digi- pins
    a.set_pin_mode(led_pin,'O')
    a.set_pin_mode(water_pump,'O')
    a.set_pin_mode(soil, 'I')
    a.set_pin_mode(pir, 'I')

    time.sleep(1)
# This is actuator program
    def water_plants():
        a.digital_write(water_pump,1)
    #read soil moisture pin
        soil_moisture= a.digital_read(5)
        print (" plants are watered")

    def light_on():
        a.digital_write(led_pin,1)

    def light_off():
        a.digital_write(led_pin,0)

    def fan_off():
        a.digital_write(fan,0)

    def fan_on():
        a.digital_write(fan,1)

    def water_null():
        a.digital_write(water_pump,0)

    
    #f= open("abc.txt", "r")
    #content= f.read()
    #f.close()

    while(True):
        #soil sensors & temp sensors are different
        soil_moisture= a.digital_read(5)
        if soil_moisture==0:
            water_plants()
        else:
            water_null()


        m =a.digital_read(pir)
        if(m==1):
            f=open("abc.txt", "r")
            content= f.read()
            f.close()
         
            while(content == 'resumed'):
                try:
                    analog_val = a.analog_read(0)
                    analog_val=int((analog_val/1023.)*100)
                    if analog_val<50 and m==1: #pir values
                        light_on()
                    else:
                        light_off()
                    temp()
                    if temperature>=27 and m==1: # for fan assign temperature
                        fan_on()
                    else:
                        fan_off()
                    m =a.digital_read(pir)
                    f=open("abc.txt", "r")
                    content= f.read()
                    f.close()

                

                except KeyboardInterrupt :
                    break
        else:
            try:
                continue
            except KeyboardInterrupt :
                break
                    
    print("Closing .....")
    a.close()        

                

        
