

from pattern import Pattern, FPS



class FadePattern(Pattern):

    def __init__(self):

        # config
        self.duration = 256


    def next(self):

        while True:

            for i in range(self.duration):

                yield (i, i, i)
