# ============================================
# RGB Lights PWM Demo - Go to (docs) for more info on this file.
# Description:
#   This script uses three GPIO pins with PWM output
#   to control an RGB LED.
#   Each color channel (Red, Green, Blue) gets a random
#   brightness value on each cycle, creating a constantly
#   changing color flow effect.
#
#   GPIO Pins:
#     - Red   : GP2
#     - Green : GP3
#     - Blue  : GP4
#
#   Frequency is set to 2000 Hz for each channel.
# ============================================

from machine import Pin, PWM
import utime
import random

# -------------------------------
# Setup: Initialize PWM for each color channel
# -------------------------------

# Red channel on GP2
Led_R = PWM(Pin(2))
Led_R.freq(2000)  # Set frequency in Hz

# Green channel on GP3
Led_G = PWM(Pin(3))
Led_G.freq(2000)

# Blue channel on GP4
Led_B = PWM(Pin(4))
Led_B.freq(2000)

# -------------------------------
# Main loop: Randomly update colors
# -------------------------------

if __name__ == "__main__":
    while True:
        # Generate random brightness for each channel (0–65535 for 16-bit PWM)
        R = random.randint(0, 65535)
        G = random.randint(0, 65535)
        B = random.randint(0, 65535)

        # Debug print for monitoring values (optional)
        print(f"R: {R}, G: {G}, B: {B}")

        # Update duty cycles
        Led_R.duty_u16(R)
        Led_G.duty_u16(G)
        Led_B.duty_u16(B)

        # Delay before next random color
        utime.sleep_ms(100)
