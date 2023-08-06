from machine import Pin, PWM
from time import sleep

U16_MAX = 65535

class Color:
    def __init__(self, gpnum):
        self.pin = PWM(Pin(gpnum))

    def duty_u16(self, duty):
        self.pin.duty_u16(duty)

    def breathe(self, interval=0.0001):
        for duty in range(0, U16_MAX, 20):
            self.duty_u16(duty)
            sleep(interval)

        for duty in range(U16_MAX, 0, -20):
            self.duty_u16(duty)
            sleep(interval)

class RGB:
    """
    Convert a traditional (8-bit) RGB color to a 16-bit color
    """
    def __init__(self, r, g, b):
        self.r = r * 256
        self.g = g * 256
        self.b = b * 256

    def to_u16(self):
        return self.r, self.g, self.b



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

    def breathe(self, sleep_interval=0.0001):
        self.R.breathe(sleep_interval)
        self.G.breathe(sleep_interval)
        self.B.breathe(sleep_interval)

    def blink(self, sleep_interval=1):
        self.on()
        print('on')
        sleep(sleep_interval)
        self.off()
        print('off')
        sleep(sleep_interval)

    def set_color(self, rgb):
        r, g, b = rgb

        if (r < 0 or r > U16_MAX):
            raise "Red value out of accepted range"

        if (g < 0 or r > U16_MAX):
            raise "Green value out of accepted range"

        if (b < 0 or b > U16_MAX):
            raise "Blue value out of accepted range"

        self.R.duty_u16(r)
        self.G.duty_u16(g)
        self.B.duty_u16(b)

    def color_cycle(self, color_list, sleep_interval=1):
        for color in color_list:
            self.set_color(color)
            sleep(sleep_interval)

COLORS = {
    'PURPLE': RGB(255, 0, 255),
    'RED': RGB(255, 0, 0),
    'GREEN': RGB(0, 255, 0),
    'BLUE': RGB(0, 0, 255)
}

def main():
    lights = StripLights()

    while True:
        lights.color_cycle([color.to_u16() for color in COLORS.values()])

    # while True:
    #     lights.breathe(0.01)

main()
