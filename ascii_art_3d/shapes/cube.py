from shapes.shape_base import ShapeBase
from shapes.point import Point3D

class Cube(ShapeBase):
    def __init__(self, size: int, color: str):
        super().__init__(color)
        self.size = size
        self.points = self.calculate_points()

    def calculate_points(self):
        points = []
        half_size = self.size / 2

        points.extend([
            Point3D(-half_size, -half_size, -half_size),
            Point3D(half_size, -half_size, -half_size),
            Point3D(half_size, half_size, -half_size),
            Point3D(-half_size, half_size, -half_size),
            Point3D(-half_size, -half_size, half_size),
            Point3D(half_size, -half_size, half_size),
            Point3D(half_size, half_size, half_size),
            Point3D(-half_size, half_size, half_size)
        ])

        return points

    def draw(self):
        lines = []
        half_size = self.size // 2

        # Верхня частина куба з перспективою
        lines.append(f"        {'*' * (self.size + 2)}")

        for i in range(half_size):
            spaces_outside = ' ' * (half_size - i)
            inner_spaces = ' ' * (self.size)
            lines.append(f"{spaces_outside}*{inner_spaces}*")

        # Завершуємо верхню частину
        lines.append(f"{' ' * (half_size)}*{'*' * (self.size)}*")

        # Бокові грані з об'ємністю
        for i in range(half_size):
            spaces_outside = ' ' * (half_size - 1)
            inner_spaces = ' ' * (self.size - 2)
            if i < half_size - 1:
                lines.append(f"{spaces_outside}*{inner_spaces}*")
            else:
                # Тінь на нижній частині
                lines.append(f"{spaces_outside}*{ '#' * (self.size - 2) }*")

        # Завершуємо нижню частину
        lines.append(f"{' ' * (half_size)}*{'*' * (self.size)}*")

        # Нижня грань з використанням символу для тіні
        lines.append(f"        {'*' * (self.size + 2)}")

        # Додаємо горизонтальні лінії для об'ємності
        for _ in range(2):  # Додаємо дві лінії
            lines.append(f"{' ' * (half_size)}*{'-' * (self.size)}*")

        return lines
