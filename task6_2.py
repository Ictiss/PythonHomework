class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self, mass, depth):
        asphalt = self._length * self._width * mass * depth
        return  asphalt

road = Road(20, 5000)
print(road.asphalt(25, 0.5))
