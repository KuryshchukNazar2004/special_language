from shapes.shape_factory import ShapeFactory
from rendering.color import Color

class Renderer:
    def __init__(self):
        self.canvas = []

    def render(self, shape_type: str, params: dict):
        shape = ShapeFactory.create_shape(shape_type, params['size'], params['color'])
        self.draw_shape(shape)

    def draw_shape(self, shape):
        # Використовуємо колір з класу Shape
        color = shape.color
        lines = shape.draw()  # Викликаємо метод draw() для отримання рядків фігури

        # Друкуємо фігуру з кольором
        for line in lines:
            colored_line = line.replace('*', Color.RED + '*' + Color.RESET)  # Змінюємо колір зірочок
            print(colored_line)
