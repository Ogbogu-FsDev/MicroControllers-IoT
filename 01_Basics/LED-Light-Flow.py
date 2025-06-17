# ============================================
# Running LEDs Demo - Go to (docs) for more info on this file.
# Description:
#   This script lights up 5 LEDs in sequence,
#   then turns them off in sequence,
#   creating a simple 'chasing lights' effect.
#
#   Each LED is connected to GPIO pins GP0 to GP4.
# ============================================

from machine import Pin    # Import Pin class for GPIO control
import utime               # MicroPython time module

# Initialize 5 GPIO pins as outputs (GP0 to GP4)
leds = [Pin(i, Pin.OUT) for i in range(5)]

if __name__ == '__main__':
    while True:
        # Turn on LEDs one by one
        for n in range(5):
            leds[n].value(1)
            utime.sleep_ms(50)

        # Turn off LEDs one by one
        for n in range(5):
            leds[n].value(0)
            utime.sleep_ms(50)
