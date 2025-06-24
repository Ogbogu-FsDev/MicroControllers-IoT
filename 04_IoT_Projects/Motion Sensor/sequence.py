from machine import Pin, PWM, Timer, I2C
import utime
import machine

inled = Pin("LED", Pin.OUT)

# PIR (Motion) Sensor
PIR = Pin(0, Pin.IN, Pin.PULL_DOWN)

# RGB LED
Led_R = PWM(Pin(4))
Led_G = PWM(Pin(3))
Led_B = PWM(Pin(2))

# Set the frequency to 2KHz
Led_R.freq(2000)  
Led_G.freq(2000)   
Led_B.freq(2000)

# Buzzer 
buzzer = PWM(Pin(15, Pin.IN)) #Sound

def LEDon(): # Onboard LED - Flash setting
    utime.sleep_ms(100)
    inled.value(1)
    utime.sleep_ms(100)
    inled.value(0)
        
def Active(): # Activating the alarm system
    if PIR.value() == 1:
        buzzer.freq(500)
        buzzer.duty_u16(1000)
        
        Led_R.duty_u16(65535)
        Led_G.duty_u16(0)
        Led_B.duty_u16(0)
        
        # Time Delay for 3 seconds
        utime.sleep(3)
        
        buzzer.duty_u16(0) # loudness set to 0 = sound off
        
        # Onboard Tempreture Sensor
        sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
        conversion_factor = 3.3 / (65535)
        
        rtc=machine.RTC()
        
        # Appending data log file with each new dection
        file = open("datalog.txt", "a")
        reading = sensor_temp.read_u16() * conversion_factor
        
        # Timestamp
        timestamp=rtc.datetime()
        temperature = 27 - (reading - 0.706)/0.001721
        timestring="Date: %04d-%02d-%02d    |    Time: %02d:%02d:%02d    |    "%(timestamp[0:3] + timestamp[4:7])
        file.write(timestring + "State: Motion Detected!    |    Temp: " + str(temperature) + "\n")
        file.flush() 
    else:
        Led_R.duty_u16(0)
        Led_G.duty_u16(65535)
        Led_B.duty_u16(0)

def InActive():
    Led_R.duty_u16(0)
    Led_G.duty_u16(0)
    Led_B.duty_u16(65535)
