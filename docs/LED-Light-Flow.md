# GPIO Pin Mapping, Circuit Diagram & Hardware Requirements

This document provides detailed information about the **GPIO pin connections**, **basic circuitry**, and **hardware components** needed to run the **LED Blinking Patterns** and other basic GPIO projects in this repository.

---

## **1️ GPIO Pin Mapping**

| Raspberry Pi Pico Pin | Purpose | Connected To |
| --------------------- | ------- | --------------------------- |
| **GP0** | Digital Output | LED1 Anode (+) via resistor |
| **GP1** | Digital Output | LED2 Anode (+) via resistor |
| **GP2** | Digital Output | LED3 Anode (+) via resistor |
| **GP3** | Digital Output | LED4 Anode (+) via resistor |
| **GP4** | Digital Output | LED5 Anode (+) via resistor |
| **GP2 (PWM)** | PWM Output | Fading LED Anode (+) via resistor |
| **GND** | Common Ground | All LED Cathodes (–) |

---

## **2️ Basic Circuit Explanation**

- **LEDs** are connected in **active high** configuration.
  - Each GPIO pin (GP0–GP4) drives the anode of an LED.
  - The cathodes of all LEDs are connected together to a **GND pin**.
- For **PWM brightness fading**, a single LED is connected to **GP2** configured as a PWM output.

**Important:**  
- Always use **current-limiting resistors** (~220Ω to 330Ω) in series with each LED’s anode to protect both the LED and the microcontroller pin.
- Make sure to double-check pin numbers with your Raspberry Pi Pico datasheet or pinout diagram.

---

## **3️ Required Hardware / Components**

| Component | Quantity | Notes |
| --------- | -------- | ------------------------------- |
| **Raspberry Pi Pico** | 1 | Microcontroller board |
| **Breadboard** | 1 | For easy prototyping |
| **LEDs** | 5 | Standard 3mm or 5mm LEDs |
| **Resistors** | 5 | ~220Ω each for current limiting |
| **Jumper Wires** | 10+ | For connections |
| **Micro USB Cable** | 1 | For flashing and power |

---

## **4️ Example Circuit Diagram**

While this repo may not include a schematic file yet, here’s a basic idea:

