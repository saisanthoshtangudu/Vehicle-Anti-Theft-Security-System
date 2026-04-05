import time
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO

# Define the LCD I2C address and I2C bus number
# Change the address if your i2cdetect command showed a different one (e.g., 0x3f)
I2C_ADDRESS = 0x27
# I2C bus number for Raspberry Pi 4 is typically 1
I2C_BUSNUM = 1

# Initialize the LCD
try:
    lcd = CharLCD(
        i2c_expander='PCF8574', 
        address=I2C_ADDRESS, 
        port=I2C_BUSNUM,
        cols=16, 
        rows=2, 
        dotsize=8
    )
except Exception as e:
    print(f"Error initializing LCD: {e}")
    print("Please check your I2C address and connections.")
    exit()


def clear():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    
def write(data):
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(data)

def main():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Hello, World!")
    
    counter = 0
    while True:
        lcd.cursor_pos = (1, 0)
        # Format the counter string and write to the second line
        lcd.write_string(f"Counter: {counter:<6}") 
        time.sleep(1)
        counter += 1
        
        # Clear the display after a certain time, if needed for complex displays
        if counter % 30 == 0:
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Counter cleared.")
            time.sleep(2)
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Hello, World!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # Clear the display and turn off the backlight on exit
        lcd.clear()
        lcd.backlight_enabled = False
        print("Program terminated and LCD cleared.")
    except Exception as e:
        print(f"An error occurred: {e}")
        lcd.clear()
        lcd.backlight_enabled = False