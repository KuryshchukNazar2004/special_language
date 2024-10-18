class ShapeBase:
    def __init__(self, color: str):
        self.color = color
        self.points = []

    def scale(self, factor: float):
        for point in self.points:
            point.x *= factor
            point.y *= factor
            point.z *= factor
