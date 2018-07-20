import unicornhathd as unicorn
import time

class Projector:
    def __init__(self, movie):
        self.movie = movie
        self.finished = False
        unicorn.brightness(0.2)
        unicorn.rotation(self.movie.rotation)

    def animate(self):
        condition = self.finished == False
        while self.finished == False:
            pixels = self.movie.step()
            for i in pixels:
                x = self.flip(i["x"])
                unicorn.set_pixel(x, i["y"], i["r"], i["g"], i["b"])
            unicorn.show()
            time.sleep(self.movie.refresh_rate)
            self.finished = self.movie.finished
        unicorn.off()

    def flip(self, x):
        """docstring for flip"""
        return x + 15 - (2 * (x % 16))

    def off(self):
        unicorn.off()
