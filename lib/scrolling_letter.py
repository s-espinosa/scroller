from letters import letters

class ScrollingLetter:
    def __init__(self):
        self.refresh_rate = 0.025
        self.finished = False
        self.rotation = 0
        self.frame    = 0
        self.heart    = letters["A"]

    def step(self):
        pixels = []
        next_frame = [0] * 256
        for index, item in enumerate(self.heart):
            x = index % 16
            y = ((index - x) / 16) % 16

            if item == 0:
                r = 0.0
                g = 0.0
                b = 0.0
            else:
                r = 255.0
                g = 255.0
                b = 255.0
            pixels.append({"x": x, "y": y, "r": r, "g": g, "b": b})
            if index % 16 == 15:
                next_position = index - 15
            else:
                next_position = index + 1
            next_frame[next_position] = item

        self.frame = self.frame + 1
        self.heart = next_frame

        return pixels

