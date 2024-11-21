from functions.functions.ConvertNumberType import ConvertNumberType
from functions.functions.ErrorHandler import GetNumber
from functions.functions.Operations import SaveToMemory

def MathOperation(choice, calc, mem):
    """
    Виконує математичну операцію на основі вибору користувача.

    Параметри:
        choice (str): Вибір користувача, що визначає операцію (1-13).
        calc (Calculator): Об'єкт калькулятора, який виконує математичні операції.
        mem (Memory): Об'єкт пам'яті для збереження та читання значень.

    Повертає:
        bool: Повертає True, якщо програма продовжує роботу, False, якщо програма повинна завершити виконання.

    Опис:
        Функція виконує математичні операції, такі як додавання, віднімання, множення, ділення тощо. 
        Якщо вибір користувача є правильним, операція виконується, і результат виводиться на екран.
        Крім того, деякі операції взаємодіють з пам'яттю калькулятора.

    Операції:
        - Операції для двох чисел (додавання, віднімання, множення, ділення, залишок, піднесення до степеня).
        - Операції для роботи з пам'яттю (додавання до пам'яті, віднімання від пам'яті).
        - Спеціальні операції: отримання історії, очищення пам'яті та виведення значень з пам'яті.
        - Вихід з калькулятора (13).

    Приклад:
        MathOperation("1", calc, mem)  # Виконує додавання двох чисел.
        MathOperation("8", calc, mem)  # Додає значення до пам'яті.
        MathOperation("13", calc, mem) # Виходить з калькулятора.

    Викидає:
        ValueError: Якщо операція виконується з некоректними значеннями (наприклад, ділення на нуль).
    """
    operations = {
        "1": lambda a, b: calc.Add(a, b),
        "2": lambda a, b: calc.Subtract(a, b),
        "3": lambda a, b: calc.Multiply(a, b),
        "4": lambda a, b: calc.Divide(a, b),
        "5": lambda a, b: calc.Mod(a, b),
        "6": lambda number, _: calc.SquareRoot(number),
        "7": lambda a, b: calc.Exponentiate(a, b),
        "8": lambda value, _: mem.Add(value),
        "9": lambda value, _: mem.Subtract(value),
    }

    if choice in operations:
        if choice in ["6"]: 
            number = ConvertNumberType(GetNumber())
            result = operations[choice](number, None)
        elif choice in ["8", "9"]: 
            value = ConvertNumberType(GetNumber())
            result = operations[choice](value, None)
            print(f"Memory value: {result}")
        else:
            a = ConvertNumberType(GetNumber())
            b = ConvertNumberType(GetNumber())
            try:
                result = operations[choice](a, b)
                print(f"Result: {result}")
                if choice not in ["8", "9"]:
                    SaveToMemory(mem, result)
            except ValueError as e:
                print(e)
                return
        if choice in ["6"]:
            print(f"Result: {result}")
            SaveToMemory(mem, result)
    elif choice in ["10", "11", "12"]:
        if choice == "10":
            print(f"Memory value: {mem.Read()}")
        elif choice == "11":
            print(f"Memory cleared: {mem.Clear()}")
        elif choice == "12":
            calc.GetHistory()
    elif choice == "13":
        print("Exiting the calculator.")
        return False
    else:
        print("Invalid choice, please try again.")
    return True
