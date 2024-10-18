from .shape_base import ShapeBase
from .point import Point3D
import math

class Sphere(ShapeBase):
    def __init__(self, radius: float = 1.0, segments: int = 8, color: str = "white"):
        super().__init__(color)
        self.radius = radius
        self.segments = segments
        self.size = radius  # Додано атрибут size
        self.points = self.calculate_points()

    def calculate_points(self):
        points = []
        for i in range(self.segments + 1):  # Додано +1, щоб закрити кільце
            phi = (i * math.pi) / self.segments  # Визначає висоту
            for j in range(self.segments * 2):
                theta = (j * 2 * math.pi) / (self.segments * 2)  # Визначає окружність
                x = self.radius * math.sin(phi) * math.cos(theta)  # Визначає x
                y = self.radius * math.cos(phi)  # Визначає y
                z = self.radius * math.sin(phi) * math.sin(theta)  # Визначає z
                points.append(Point3D(x, y, z))
        return points
