class UserInput:
    """
    Клас для обробки введення користувача та взаємодії з кубом.

    Атрибути:
        cube (Cube): Об'єкт класу Cube для маніпуляцій з кубом.
        colors (dict): Словник доступних кольорів, які можна застосувати до куба.
    """

    def __init__(self, cube):
        """
        Ініціалізує об'єкт UserInput.

        Параметри:
            cube (Cube): Об'єкт куба, з яким взаємодіятиме користувач.
        """
        self.cube = cube
        self.colors = {
            "1": "Red", "2": "Green", "3": "Blue", "4": "Yellow", "5": "Cyan", 
            "6": "Magenta", "7": "White", "8": "Black", "9": "Gray", "10": "Orange"
        }

    def get_next_action(self):
        """
        Отримує наступну дію від користувача.

        Повертає:
            str: Вибір дії користувача.
        """
        try:
            print("\nWhat do you want to do next?\n1 - Rotate\n2 - Change Color\n3 - Scale\n4 - Save to File\n5 - Exit")
            choice = input("Your choice: ")
            return choice
        except Exception as e:
            print(f"Error getting action input: {e}")
            return None

    def get_rotation_input(self):
        """
        Отримує кути обертання для куба від користувача.

        Запитує у користувача значення кутів обертання по осях X та Y.

        Виключення:
            ValueError: Якщо введені значення не є числовими.
        """
        try:
            angle_x = float(input("Enter X rotation angle (between -360 and 360): "))
            angle_y = float(input("Enter Y rotation angle (between -360 and 360): "))
            self.cube.set_rotation(angle_x, angle_y)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"Error in rotation input: {e}")

    def get_scale_input(self):
        """
        Отримує фактор масштабу для куба від користувача.

        Запитує у користувача значення для масштабування куба.

        Виключення:
            ValueError: Якщо введене значення не є числовим.
        """
        try:
            scale = float(input("Enter scale factor (between 1 and 100): "))
            if scale > 0:
                self.cube.set_scale(scale)
            else:
                print("Scale factor must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"Error in scale input: {e}")

    def get_initial_size(self):
        """
        Отримує початкові розміри куба від користувача.

        Параметри:
            (None)

        Повертає:
            tuple: Розміри куба по осях X, Y, Z, обмежені діапазоном від 1 до 13.
        """
        try:
            size_x = float(input("Enter the cube size along X-axis (between 1 and 13): "))
            size_y = float(input("Enter the cube size along Y-axis (between 1 and 13): "))
            size_z = float(input("Enter the cube size along Z-axis (between 1 and 13): "))
            # Обмежуємо розміри між 1 і 13
            size_x = max(1, min(13, size_x))
            size_y = max(1, min(13, size_y))
            size_z = max(1, min(13, size_z))
            return size_x, size_y, size_z
        except ValueError:
            print("Invalid input. Default size 10x10x10 will be used.")
            return 10, 10, 10
        except Exception as e:
            print(f"Error getting initial size: {e}")
            return 10, 10, 10

    def change_color(self):
        """
        Змінює колір куба, залежно від вибору користувача.

        Параметри:
            (None)

        Повертає:
            (None)
        """
        try:
            print("Available colors: ")
            for key, color in self.colors.items():
                print(f"{key}: {color}")

            choice = input("Choose a color by entering a number: ")
            if choice in self.colors:
                self.cube.color = self.colors[choice]
                print(f"Color changed to {self.colors[choice]}")
            else:
                print("Invalid choice. Default color remains.")
        except Exception as e:
            print(f"Error changing color: {e}")
