import numpy as np
from shapes.shape_base import ShapeBase
from rendering.color import Color

class Pyramid(ShapeBase):
    def __init__(self, size: int, color: str = "white"):
        super().__init__(color)
        self.size = size  # Розмір піраміди

    def draw(self):
        height = self.size
        base_width = 2 * height + 1
        
        # Створюємо порожню матрицю для канвасу
        canvas = np.full((height + 1, base_width), ' ')

        # Додаємо верхню частину піраміди
        for i in range(height):
            stars = '*' * (2 * i + 1)
            left_padding = height - i - 1
            canvas[i, left_padding:left_padding + len(stars)] = list(stars)

        # Додаємо бічні грані
        for i in range(height):
            if i == height - 1:
                # Основна частина (основа піраміди)
                canvas[height, :] = '*'
            else:
                left_side = height - 1 - i
                canvas[i + 1, left_side] = '*'
                canvas[i + 1, base_width - left_side - 1] = '*'

        return canvas

    def render(self):
        pyramid = self.draw()
        for line in pyramid:
            # Перетворюємо кожен рядок у рядок
            line_str = ''.join(line.tolist())  # Змінено на tolist() і join
            colored_line = line_str.replace('*', Color.RED + '*' + Color.RESET)  # Застосовуємо колір
            print(colored_line)
