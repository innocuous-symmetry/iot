from machine import Pin, PWM, freq
from time import sleep

U16_MAX = 65535

class Color:
    def __init__(self, gpnum):
        self.pin = PWM(Pin(gpnum))

    def duty_u16(self, duty):
        self.pin.duty_u16(duty)

    def breathe(self):
        for duty in range(0, U16_MAX, 20):
            self.duty_u16(duty)
            sleep(0.0001)

        for duty in range(U16_MAX, 0, -20):
            self.duty_u16(duty)
            sleep(0.0001)


class StripLights:
    def __init__(self):
        self.B = Color(10)
        self.R = Color(11)
        self.G = Color(12)

    def on(self):
        self.R.duty_u16(U16_MAX)
        self.G.duty_u16(U16_MAX)
        self.B.duty_u16(U16_MAX)

    def off(self):
        self.R.duty_u16(0)
        self.G.duty_u16(0)
        self.B.duty_u16(0)

    def breathe(self):
        self.R.breathe()
        self.G.breathe()
        self.B.breathe()

    def blink(self, sleep_interval=1):
        self.on()
        print('on')
        sleep(sleep_interval)
        self.off()
        print('off')
        sleep(sleep_interval)

    def set_color(self, r, g, b):
        if (r < 0 or r > U16_MAX):
            raise "Red value out of accepted range"

        if (g < 0 or r > U16_MAX):
            raise "Green value out of accepted range"

        if (b < 0 or b > U16_MAX):
            raise "Blue value out of accepted range"

        self.R.duty_u16(r)
        self.G.duty_u16(g)
        self.B.duty_u16(b)

def main():
    lights = StripLights()

    while True:
        lights.blink()

main()
