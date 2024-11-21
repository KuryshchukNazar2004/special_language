from models.cube import Cube
from render.renderer import Renderer
from controllers.user_input import UserInput
import os
import time

if __name__ == "__main__":
    """
    Головний виконавчий модуль для створення та рендерингу 3D-куба.

    Опис:
    Ця програма дозволяє користувачеві взаємодіяти з 3D-кубом, виконувати операції, такі як обертання, зміна кольору, масштабування, а також збереження поточного стану куба у файл.

    Кроки роботи програми:
    1. Запитує у користувача початковий розмір куба.
    2. Створює об'єкт куба заданого розміру.
    3. Використовує рендерер для візуалізації обертів куба у вигляді ASCII-арту.
    4. Дозволяє користувачеві взаємодіяти з кубом, виконуючи різні операції, включаючи обертання, зміну кольору, масштабування і збереження куба.
    5. Завершує програму при виборі користувачем відповідної опції.

    Параметри:
        None
    Повертає:
        None
    """

    # Створення об'єкта для введення користувача
    user_input = UserInput(None)

    # Отримання початкових розмірів куба
    size_x, size_y, size_z = user_input.get_initial_size()
    cube = Cube(size_x, size_y, size_z)  # Створення куба з заданими розмірами
    user_input.cube = cube  # Зв'язок куба з об'єктом вводу

    # Ініціалізація рендерера для візуалізації
    renderer = Renderer(resolution=40, foco=40, y_distorter=1.1, left_right=1.5, up_down=0.5)

    try:
        while True:
            # Очищення екрану перед наступним рендером
            os.system('cls' if os.name == 'nt' else 'clear')

            # Отримання обертів куба та проекція
            rotated_cube = cube.rotate()
            projection = renderer.project(rotated_cube)

            # Генерація ASCII-арту куба
            lines = renderer.get_lines(projection)
            rendered_ascii = renderer.render(projection, lines, cube.color)
            
            # Виведення рендереного куба на екран
            print(rendered_ascii)
            time.sleep(0.5)  # Затримка для відображення

            # Запит на наступну дію користувача
            action = user_input.get_next_action()

            # Обробка різних варіантів дій
            if action == "1":
                user_input.get_rotation_input()  # Обертання куба
            elif action == "2":
                user_input.change_color()  # Зміна кольору куба
            elif action == "3":
                user_input.get_scale_input()  # Масштабування куба
            elif action == "4":
                filename = input("Enter filename to save the cube: ")  # Збереження куба у файл
                cube.save_to_file(filename, rendered_ascii)
            elif action == "5":
                print("Exiting...")  # Завершення програми
                break
            else:
                print("Invalid choice. Try again.")  # Невірний вибір
    except KeyboardInterrupt:
        print("Program interrupted.")  # Вихід при натисканні Ctrl+C

