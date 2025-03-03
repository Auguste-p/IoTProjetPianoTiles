from machine import Pin, ADC
import time
from ServoController import ServoController

# Analog input pins
IN_D2 = ADC(Pin(32))  # Changed to valid pin for ESP32
IN_D0 = ADC(Pin(23))  # Changed to valid pin for ESP32
IN_D1 = ADC(Pin(34))  # Changed to valid pin for ESP32
IN_D3 = ADC(Pin(35))  # Changed to valid pin for ESP32<

# Servo motor pins
servo_pins = [13, 12, 14, 27]
servo_controller = ServoController(servo_pins)

def setup():
    pass  # No setup needed for console output

def loop():
    while True:
        value_D0 = IN_D0.read()
        value_D2 = IN_D2.read()
        value_D1 = IN_D1.read()
        value_D3 = IN_D3.read()

        print("D2:{}".format(value_D2))
        print("D0:{}".format(value_D0))
        print("D1:{}".format(value_D1))
        print("D3:{}".format(value_D3))

        if value_D0 > 1000:
            servo_controller.set_servo_on(0)
            time.sleep(0.1)
            servo_controller.set_servo_off(0)
            print("Servo 0 on")
        else:
            servo_controller.set_servo_off(0)

        if value_D1 > 1000:
            servo_controller.set_servo_on(1)
            time.sleep(0.2)
            print("Servo 1 on")
            servo_controller.set_servo_off(1)
        else:
            servo_controller.set_servo_off(1)

        if value_D2 > 1000:
            servo_controller.set_servo_on(2)
            time.sleep(0.2)
            print("Servo 2 on")
            servo_controller.set_servo_off(2)
        else:
            servo_controller.set_servo_off(2)

        if value_D3 > 2000:
            servo_controller.set_servo_on(3)
            time.sleep(0.2)
            print("Servo 3 on")
            servo_controller.set_servo_off(3)
        else:
            servo_controller.set_servo_off(3)

        time.sleep(0.2)

setup()
loop()
