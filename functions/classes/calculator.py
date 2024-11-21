import math

class Calculator:
    """
    Клас для виконання основних математичних операцій, таких як додавання, віднімання, множення, ділення, 
    знаходження залишку від ділення, квадратний корінь та піднесення до степеня.

    Атрибути:
        None
    
    Методи:
        Save(value): Зберігає результат операції в історії (файл 'History.txt').
        Add(a, b): Додає два числа та зберігає результат.
        Subtract(a, b): Віднімає два числа та зберігає результат.
        Multiply(a, b): Множить два числа та зберігає результат.
        Divide(a, b): Ділить два числа, якщо дільник не нуль, та зберігає результат.
        Mod(a, b): Знаходить залишок від ділення двох чисел та зберігає результат.
        SquareRoot(number): Знаходить квадратний корінь числа та зберігає результат.
        Exponentiate(a, b): Підносить число до степеня та зберігає результат.
        GetHistory(): Виводить історію виконаних операцій із файлу 'History.txt'.
    """

    def Save(self, value):
        """
        Зберігає результат операції в історії.

        Параметри:
            value (str): Текст, який потрібно записати в файл.

        Файл:
            'History.txt' - файл, в який додаються нові записи.
        """
        with open('History.txt', 'a') as file:
            file.write(f"{value}\n")

    def Add(self, a, b):
        """
        Додає два числа та зберігає результат в історії.

        Параметри:
            a (float): Перше число.
            b (float): Друге число.

        Повертає:
            float: Результат додавання.
        """
        result = a + b
        self.Save(f"{a} + {b} = {result}")
        return result

    def Subtract(self, a, b):
        """
        Віднімає два числа та зберігає результат в історії.

        Параметри:
            a (float): Перше число.
            b (float): Друге число.

        Повертає:
            float: Результат віднімання.
        """
        result = a - b
        self.Save(f"{a} - {b} = {result}")
        return result

    def Multiply(self, a, b):
        """
        Множить два числа та зберігає результат в історії.

        Параметри:
            a (float): Перше число.
            b (float): Друге число.

        Повертає:
            float: Результат множення.
        """
        result = a * b
        self.Save(f"{a} * {b} = {result}")
        return result

    def Divide(self, a, b):
        """
        Ділить два числа та зберігає результат в історії, якщо дільник не нуль.

        Параметри:
            a (float): Число, яке потрібно поділити.
            b (float): Число, на яке потрібно поділити.

        Повертає:
            float: Результат ділення.

        Викидає:
            ValueError: Якщо дільник є нулем.
        """
        if b != 0:
            result = a / b
            self.Save(f"{a} / {b} = {result}")
            return result
        else:
            raise ValueError("Division by zero is not allowed")

    def Mod(self, a, b):
        """
        Знаходить залишок від ділення двох чисел та зберігає результат в історії.

        Параметри:
            a (float): Число, яке потрібно поділити.
            b (float): Число, на яке потрібно поділити.

        Повертає:
            float: Залишок від ділення.
        """
        result = a % b
        self.Save(f"{a} % {b} = {result}")
        return result

    def SquareRoot(self, number):
        """
        Знаходить квадратний корінь числа та зберігає результат в історії.

        Параметри:
            number (float): Число, для якого потрібно знайти квадратний корінь.

        Повертає:
            float: Квадратний корінь числа.
        """
        result = math.sqrt(number)
        self.Save(f"Square root of {number} = {result}")
        return result

    def Exponentiate(self, a, b):
        """
        Підносить число до степеня та зберігає результат в історії.

        Параметри:
            a (float): Число, яке потрібно піднести до степеня.
            b (float): Степінь.

        Повертає:
            float: Результат піднесення до степеня.
        """
        result = a ** b
        self.Save(f"{a}^{b} = {result}")
        return result

    def GetHistory(self):
        """
        Виводить історію виконаних операцій з файлу 'History.txt'.

        Повертає:
            str: Вміст файлу історії.
        """
        with open("History.txt", "r") as file:
            return print(file.read())


class Memory(Calculator):
    """
    Клас для роботи з пам'яттю калькулятора. Наслідує методи класу Calculator, додаючи можливості для 
    збереження та роботи з значенням пам'яті.

    Атрибути:
        value (float): Поточне значення в пам'яті.

    Методи:
        Add(value): Додає значення до поточної пам'яті.
        Subtract(value): Віднімає значення від поточної пам'яті.
        Clear(): Очищає пам'ять.
        Read(): Читає поточне значення в пам'яті.
    """

    def __init__(self):
        """
        Ініціалізує пам'ять з початковим значенням 0.
        """
        super().__init__()
        self.value = 0

    def Add(self, value):
        """
        Додає значення до поточної пам'яті та зберігає в історії.

        Параметри:
            value (float): Значення для додавання до пам'яті.

        Повертає:
            float: Поточне значення в пам'яті після додавання.
        """
        self.value += value
        self.Save(f"Memory added: {self.value}")
        return self.value

    def Subtract(self, value):
        """
        Віднімає значення від поточної пам'яті та зберігає в історії.

        Параметри:
            value (float): Значення для віднімання від пам'яті.

        Повертає:
            float: Поточне значення в пам'яті після віднімання.
        """
        self.value -= value
        self.Save(f"Memory subtracted: {self.value}")
        return self.value

    def Clear(self):
        """
        Очищає пам'ять та зберігає результат в історії.

        Повертає:
            float: Поточне значення в пам'яті після очищення.
        """
        self.value = 0
        self.Save("Memory cleared")
        return self.value

    def Read(self):
        """
        Читає поточне значення в пам'яті.

        Повертає:
            float: Поточне значення в пам'яті.
        """
        return self.value
