# RGB Light Show — Random Color Generator

This project demonstrates how to control an RGB LED using PWM on a Raspberry Pi Pico. The script randomly changes the brightness of each color channel (Red, Green, and Blue) to produce an endless sequence of smooth, unpredictable colors, creating a simple yet eye-catching light show.

---

## File

- `RGB-Light-Show.py` — Main script controlling the RGB LED

---

## Features

- Uses hardware PWM to smoothly control the brightness of each color channel
- Generates new random values every 100 ms for continuous color transitions
- Easy to customize: adjust frequency, update rate, or use different GPIO pins
- Educational: demonstrates PWM, random number generation, and GPIO usage in MicroPython

---

## Pinout

| GPIO Pin | Color Channel | Connected To |
| -------- | -------------- | -------------- |
| GP2 | Red | Red Anode via resistor |
| GP3 | Green | Green Anode via resistor |
| GP4 | Blue | Blue Anode via resistor |
| GND | Common Ground | RGB LED cathode (for common cathode type) |

---

## Circuit Requirements

**Components:**

| Item | Quantity | Notes |
| ---- | -------- | ----- |
| RGB LED | 1 | Common cathode or common anode |
| Resistors | 3 | Approximately 220Ω each for Red, Green, and Blue |
| Raspberry Pi Pico | 1 | Microcontroller board |
| Breadboard & Jumper Wires | — | For easy prototyping |

**Wiring tips:**

- If using a common cathode RGB LED, connect the cathode to Pico GND.
- If using a common anode RGB LED, connect the anode to 3.3V and invert the PWM logic (requires minor code changes).

---

## How It Works

1. Each PWM pin controls one color channel’s brightness.
2. Every loop iteration, the script picks a random duty cycle (0–65535) for each channel.
3. The LED blends these to create a mixed color.
4. Updates happen every 100 milliseconds for a smooth show.

---

## How To Run

1. Wire the RGB LED and resistors to GPIO pins GP2, GP3, and GP4.
2. Connect the cathode to GND.
3. Flash `RGB-Light-Show.py` to your Pico using Thonny or any MicroPython tool.
4. Observe the LED continuously changing colors.

---

## Example Output

Sample console output:
R: 10234, G: 54321, B: 32411
R: 20455, G: 23211, B: 65535

This shows the raw 16-bit PWM values for each channel.

---

## Customization Tips

- Change `Led_R.freq(2000)` to a higher or lower value for different LED response.
- Adjust `utime.sleep_ms(100)` to make the color change faster or slower.
- Use smoother transitions by interpolating instead of random jumps (an interesting extension to try).

---

## License

This project is open-source and free to modify for learning or personal use. Attribution is appreciated.

