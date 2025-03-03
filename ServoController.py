from machine import Pin, PWM

class ServoController:
    def __init__(self, pins):
        self.servos = [PWM(Pin(pin), freq=50) for pin in pins]

    def set_servo_angle(self, index, angle):
        duty = int((angle / 180) * 1023 + 26)
        self.servos[index].duty(duty)

    def set_servo_on(self, index):
        self.servos[index].duty(70)  # Set duty cycle to turn the servo on
        print("servo on ")

def set_servo_off(self, index):
    self.servos[index].duty(90)  # Set duty cycle to turn the servo off

