import faces as fc
import gpio as gpio
import time
import lcd as dis
import threading
import mail as gmail
import gpsModule as gps

###--------------------Things to be modified---------------
duration = 60
SenderMailID = "your_email@gmail.com"
passkey = 'xxxx xxxx xxxx xxxx'
DestinationMailID = "receiver_email@gmail.com"

###---------------------------------------------------------


STOP_PIN = 24
IGNITION_PIN = 17
RELAY_PIN = 23
SHOCK_PIN = 22
BUZZER_PIN = 27

gmail.mail_init(SenderMailID,passkey,DestinationMailID)
unknown = True


def mailGPS(stop_event):
    while not stop_event.is_set():
        location = gps.getLocation(5)
        gmail.SendMail(location)
        #time.sleep(duration)
        stop_event.wait(duration) 

def main():
    global unkown
    dis.write("press Ign to start")
    stop_signal = threading.Event()
    t1 = threading.Thread(target=mailGPS, args=(stop_signal,))
    t1.start()
    #t1.join()
    while(True): 
        if gpio.read_pin(IGNITION_PIN):
            dis.write("Scanning..Please Face the camera")
            if (fc.scan() == False):
                dis.write("Unknown person       Detected")
                print("unknown")
                gpio.set_pin(SHOCK_PIN)
                time.sleep(1)
                gpio.clear_pin(SHOCK_PIN)
                gpio.clear_pin(BUZZER_PIN)
                time.sleep(5)
                gpio.set_pin(BUZZER_PIN)
                gpio.clear_pin(RELAY_PIN)
                dis.write("press Ign to start")
                t1 = threading.Thread(target=mailGPS, args=(stop_signal,))
                t1.start()
            else:
                stop_signal.set()
                unknown = False
                dis.write("Known person       Detected")
                print("good")
                time.sleep(2)
                dis.clear()
                dis.write("Vehicle is in   ACTIVE Mode")
                gpio.set_pin(RELAY_PIN)
                
                
                
            #print("Press the Ignition Button to start")
        if gpio.read_pin(STOP_PIN):
            t1.start()
            gpio.clear_pin(RELAY_PIN)
            dis.write("press Ign to start")


if __name__ == "__main__":
    main()
