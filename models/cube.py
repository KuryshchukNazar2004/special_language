from math import cos, sin, radians
from numpy import dot
import re

class Cube:
    """
    Клас для створення та маніпулювання 3D-кубом.

    Атрибути:
        corners (list): Список, що містить координати восьми вершин куба.
        angle_x (float): Кут обертання куба по осі X.
        angle_y (float): Кут обертання куба по осі Y.
        scale (float): Масштаб куба.
        color (str): Колір куба.
    """
    def __init__(self, size_x=10, size_y=10, size_z=10, angle_x=0, angle_y=0, scale=1, color="White"):
        """
        Ініціалізує об'єкт куба.

        Параметри:
            size_x (float): Розмір куба по осі X.
            size_y (float): Розмір куба по осі Y.
            size_z (float): Розмір куба по осі Z.
            angle_x (float): Кут обертання по осі X.
            angle_y (float): Кут обертання по осі Y.
            scale (float): Масштаб куба.
            color (str): Колір куба.
        """
        self.corners = [[-size_x, -size_y, -size_z], [size_x, -size_y, -size_z],
                        [-size_x, -size_y, size_z], [-size_x, size_y, -size_z],
                        [size_x, -size_y, size_z], [size_x, size_y, -size_z],
                        [-size_x, size_y, size_z], [size_x, size_y, size_z]]
        self.angle_x = angle_x
        self.angle_y = angle_y
        self.scale = scale
        self.color = color

    def rotate(self):
        """
        Обертає куб на задані кути по осях X та Y.

        Повертає:
            list: Перераховані координати вершин куба після обертання.
        """
        x_rotator = [[1, 0, 0],
                     [0, cos(radians(self.angle_x)), sin(radians(self.angle_x))],
                     [0, -sin(radians(self.angle_x)), cos(radians(self.angle_x))]]
        y_rotator = [[cos(radians(self.angle_y)), 0, -sin(radians(self.angle_y))],
                     [0, 1, 0],
                     [sin(radians(self.angle_y)), 0, cos(radians(self.angle_y))]]
        rotated_cube = [dot(dot(point, x_rotator), y_rotator) for point in self.corners]
        return self.scale_cube(rotated_cube)

    def scale_cube(self, cube):
        """
        Масштабує куб за заданим масштабом.

        Параметри:
            cube (list): Список з координатами точок, що визначають куб.

        Повертає:
            list: Масштабовані координати точок.
        """
        return [[point[0] * self.scale, point[1] * self.scale, point[2] * self.scale] for point in cube]

    def set_rotation(self, angle_x, angle_y):
        """
        Встановлює кути обертання для куба по осях X та Y.

        Параметри:
            angle_x (float): Кут обертання по осі X.
            angle_y (float): Кут обертання по осі Y.
        """
        self.angle_x = max(-360, min(360, angle_x))
        self.angle_y = max(-360, min(360, angle_y))

    def set_scale(self, scale):
        """
        Встановлює масштаб куба.

        Параметри:
            scale (float): Масштаб куба. Має бути між 1 і 5.
        """
        if 1 <= scale <= 5:
            self.scale = scale
        else:
            print("Invalid scale. It must be between 1 and 5.")
    
    def save_to_file(self, filename, rendered_ascii):
        """
        Зберігає ASCII-арт куба у файл.

        Параметри:
            filename (str): Назва файлу для збереження.
            rendered_ascii (str): ASCII-арт куба.
        """
        # Видалення всіх ANSI-кодів (форматування, кольори, стилі)
        clean_ascii = re.sub(r'\033\[\d+;?\d*;?\d*m', '', rendered_ascii)  
        with open(f"{filename}.txt", "w") as file:
            file.write(clean_ascii)
        print(f"Cube saved to {filename}.txt")
