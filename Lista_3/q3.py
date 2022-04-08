class House(object):
    def __init__(self, height, colors):
        self.height = height
        self.colors = colors


class Kitchen(House):
    def __init__(self, height, colors, supplies):
        super().__init__(height, colors)
        self.supplies = supplies


class Bedroom(House):
    def __init__(self, height, colors, furniture):
        super().__init__(height, colors)
        self.furniture = furniture
