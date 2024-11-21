import os
import time

def run_application(user_input, cube, renderer):
    actions = {
        "1": user_input.get_rotation_input,
        "2": user_input.change_color,
        "3": user_input.get_scale_input,
        "4": save_cube_to_file,  # Новий метод для збереження
        "5": exit_application
    }
    
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            rotated_cube = cube.rotate()
            projection = renderer.project(rotated_cube)
            lines = renderer.get_lines(projection)
            rendered_ascii = renderer.render(projection, lines, cube.color)
            time.sleep(0.5)
            action = user_input.get_next_action()

            # Використання словника для дій
            if action in actions:
                if action == "4":
                    filename = input("Enter filename to save the cube: ")
                    actions[action](cube, filename)  # Передача аргументів
                else:
                    actions[action]()  # Виклик функції без аргументів
            elif action == "5":
                actions[action]()  # Виклик функції для виходу
            else:
                print("Invalid choice. Try again.")
    except KeyboardInterrupt:
        print("Program interrupted.")

def save_cube_to_file(cube, filename):
    try:
        cube.save_to_file(filename, rendered_ascii)
        print(f"Cube saved to {filename}.")
    except Exception as e:
        print(f"Error saving cube: {e}")

def exit_application():
    print("Exiting...")
    exit(0)  # Завершення програми
