from functions.classes.calculator import Calculator, Memory
from functions.functions.Menu import DisplayMenu 
from functions.functions.MathOperation import MathOperation

def main():
    """
    Головна функція для виконання калькулятора.

    Створює об'єкти класів Calculator та Memory, потім запускає цикл 
    введення, в якому користувач може вибирати операції для виконання 
    через меню. Програма працює до тих пір, поки користувач не вибере 
    опцію для завершення.

    Процес:
        1. Створюється об'єкт калькулятора та об'єкт пам'яті.
        2. Виводиться меню користувачу.
        3. Користувач вибирає операцію, яка буде виконана.
        4. Якщо операція не завершує програму, цикл продовжується.
    """
    calc = Calculator()  # Ініціалізація калькулятора
    mem = Memory()  # Ініціалізація пам'яті

    while True:
        DisplayMenu()  # Виведення меню для вибору операції
        choice = input("Select an operation (1-13): ")
        
        # Виконання операції відповідно до вибору користувача
        if not MathOperation(choice, calc, mem):
            break  # Завершення циклу, якщо вибір користувача вказує на вихід

if __name__ == "__main__":
    main()
