from shapes.cube import Cube
from shapes.sphere import Sphere
from shapes.pyramid import Pyramid

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, size: int, color: str):
        if shape_type == 'cube':
            return Cube(size, color)
        elif shape_type == 'sphere':
            segments = max(8, size // 2)  # Ensure segments are appropriate
            return Sphere(size, segments, color)
        elif shape_type == 'pyramid':
            return Pyramid(size, color)  # Create Pyramid with size and color
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
