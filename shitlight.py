

import RPi.GPIO as GPIO


class Dashboard():

    def __init__(self):

        # self.pins = [ 2, 3, 4, 14, 15, 17, 18, 27, 22 ]
        self.pins = [ 2, 14, 18, 3, 15, 27, 4, 17, 22 ]

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        for i in self.pins:
            GPIO.setup(i, GPIO.OUT)


    def set_color(self, colors):
        # list of rgb tuples

        assert len(colors) == len(self.pins)

        for i, color in enumerate(colors):
            # tuple of rgb values (int)

            if isinstance(color, tuple):
                color = sum(color)

            if color > 0:
                GPIO.output(self.pins[i], GPIO.HIGH)
            else:
                GPIO.output(self.pins[i], GPIO.LOW)

