# ===========================
# Onboard LED Speed Pattern Demo
# Description:
#   This script demonstrates how to blink an onboard LED
#   on a Raspberry Pi Pico at different speeds:
#   fast, medium, and slow — cycling through each pattern
#   continuously.
#
#   It shows how to use functions, loops, and GPIO control
#   in MicroPython for simple timing-based tasks.
# ===========================

from machine import Pin      # Import Pin class for GPIO control
import utime                 # Import MicroPython time module (utime)

# Initialize onboard LED (Pin 25 for Raspberry Pi Pico)
led = Pin(25, Pin.OUT)

def blink(delay_ms, repeats):
    """
    Blink the LED ON and OFF.
    :param delay_ms: Time in milliseconds for ON and OFF states.
    :param repeats: Number of blink cycles to perform.
    """
    for _ in range(repeats):
        led.value(1)               # Turn LED ON
        utime.sleep_ms(delay_ms)   # Wait for delay
        led.value(0)               # Turn LED OFF
        utime.sleep_ms(delay_ms)   # Wait again

def fast():
    """
    Fast blink pattern.
    ON/OFF every 100 ms, repeated 10 times.
    """
    blink(100, 10)

def medium():
    """
    Medium-speed blink pattern.
    ON/OFF every 300 ms, repeated 10 times.
    """
    blink(300, 10)

def slow():
    """
    Slow blink pattern.
    ON/OFF every 600 ms, repeated 10 times.
    """
    blink(600, 10)

if __name__ == '__main__':
    # Infinite loop: cycle through fast, medium, slow patterns
    while True:
        fast()     # Blink fast
        medium()   # Then blink medium
        slow()     # Then blink slow
        # The cycle repeats continuously
