from letters import letters

class ScrollingMessage:
    def __init__(self, message):
        self.refresh_rate = 0.015
        self.finished = False
        self.rotation = 0
        self.frame    = 0
        self.message  = self.encode(message)

    def encode(self, message):
        """docstring for encode"""
        upcased    = message.upper()
        padded     = upcased + "  "
        characters = list(padded)
        encoded    = list(map(lambda letter: letters[letter], characters))
        split_letters = list(map(lambda letters: list(self.split(letters, 16)), encoded))
        joined_letters = self.join_rows(split_letters)
        flattened      = self.flatten_rows(joined_letters)
        return flattened

    def split(self, encoded_letters, n):
        """docstring for split"""
        for i in range(0, len(encoded_letters), n):
            yield encoded_letters[i:i + n]

    def join_rows(self, split_letters):
        """docstring for join_rows"""
        row = []
        for i in range(0, 16):
            building = []
            for j in split_letters:
                building = building + j[i]
            row.append(building)
        return row

    def flatten_rows(self, joined_letters):
        """docstring for flatten_rows"""
        flat_list = []
        for sublist in joined_letters:
            for item in sublist:
                flat_list.append(item)
        return flat_list

    def step(self):
        self.shift_numbers()
        single = self.get_single()
        self.frame = self.frame + 1
        return self.generate_pixels(single)

    def shift_numbers(self):
        """docstring for shift_pixels"""
        characters  = len(self.message) / 256
        line_length = 16 * characters
        next_frame  = [0] * (256 * characters)

        for index, item in enumerate(self.message):
            if index % line_length == 0:
                next_position = index + (line_length - 1)
            else:
                next_position = index - 1
            next_frame[next_position] = item

        self.message = next_frame

    def get_single(self):
        """docstring for get_single"""
        characters  = len(self.message) / 256
        line_length = 16 * characters
        starts = []
        for i in range(0, 16):
            starts.append(i * characters * 16)

        rows = list(map(lambda x: self.message[x:(x+16)], starts))
        flat_list = []
        for sublist in rows:
            for item in sublist:
                flat_list.append(item)
        return(flat_list)

    def generate_pixels(self, numbers):
        """docstring for generate_pixels"""
        pixels = []

        for index, item in enumerate(numbers):
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
        return pixels

