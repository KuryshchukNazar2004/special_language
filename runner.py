import os
import time

def run_application(user_input, cube, renderer):
    """
    Основний цикл програми для виконання дій з кубом та його рендерингу.
    
    Параметри:
        user_input (UserInput): Об'єкт класу UserInput для збору введення користувача.
        cube (Cube): Об'єкт класу Cube для роботи з кубом.
        renderer (Renderer): Об'єкт класу Renderer для рендерингу проекцій куба.
    
    Виконує циклічну обробку введення користувача та рендеринг куба, поки користувач не вибере вихід.
    """
    # Словник для зв'язку введення користувача з відповідними методами
    actions = {
        "1": user_input.get_rotation_input,  # Виклик методу для обертання куба
        "2": user_input.change_color,  # Виклик методу для зміни кольору куба
        "3": user_input.get_scale_input,  # Виклик методу для масштабування куба
        "4": save_cube_to_file,  # Метод для збереження куба у файл
        "5": exit_application  # Метод для виходу з програми
    }
    
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Очищення екрану для нового рендеру
            rotated_cube = cube.rotate()  # Обертання куба
            projection = renderer.project(rotated_cube)  # Отримання проекції куба
            lines = renderer.get_lines(projection)  # Отримання ліній для проекції
            rendered_ascii = renderer.render(projection, lines, cube.color)  # Рендеринг у вигляді ASCII-арту
            time.sleep(0.5)  # Затримка для оновлення екрану
            action = user_input.get_next_action()  # Отримання наступної дії користувача

            # Використання словника для виконання дії
            if action in actions:
                if action == "4":
                    filename = input("Enter filename to save the cube: ")  # Запит на ім'я файлу
                    actions[action](cube, filename)  # Виклик функції для збереження куба
                else:
                    actions[action]()  # Виклик функції без параметрів (для обертання, зміни кольору, тощо)
            elif action == "5":
                actions[action]()  # Виклик функції для виходу з програми
            else:
                print("Invalid choice. Try again.")  # Виведення повідомлення при неправильному виборі
    except KeyboardInterrupt:
        print("Program interrupted.")  # Обробка переривання програми за допомогою Ctrl+C

def save_cube_to_file(cube, filename):
    """
    Зберігає поточний стан куба у файл.

    Параметри:
        cube (Cube): Об'єкт класу Cube для збереження.
        filename (str): Назва файлу для збереження куба.
    
    Викидає:
        Exception: Якщо виникає помилка під час збереження.
    """
    try:
        cube.save_to_file(filename, rendered_ascii)  # Збереження куба в ASCII-форматі
        print(f"Cube saved to {filename}.")  # Повідомлення про успішне збереження
    except Exception as e:
        print(f"Error saving cube: {e}")  # Обробка помилки під час збереження

def exit_application():
    """
    Завершує роботу програми.
    """
    print("Exiting...")
    exit(0)  # Завершення програми
