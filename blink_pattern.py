

from pattern import Pattern, FPS



class BlinkPattern(Pattern):

    def __init__(self):

        # config
        self.duration_on = FPS
        self.duration_off = FPS
        self.color = (255, 255, 0)
        self.black = (0  ,   0, 0)


    def next(self):

        while True:

            for i in range(self.duration_on + self.duration_off):

                if i < self.duration_on:
                    yield self.color
                else:
                    yield self.black
