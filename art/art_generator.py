import pyfiglet
from colorama import Fore, Style
from art.config import COLOR_MAP

def generate_ascii_art(text, font, color, width, height, symbol):
    """
    Генерує ASCII-арт із заданими параметрами.

    Параметри:
        text (str): Текст, який буде перетворено в ASCII-арт.
        font (str): Шрифт для генерації ASCII-арту.
        color (str): Колір ASCII-арту (наприклад, 'red', 'green', 'yellow').
        width (int): Ширина результату ASCII-арту.
        height (int): Висота результату ASCII-арту.
        symbol (str): Символ, який буде використовуватися для заповнення пробілів в ASCII-арті.

    Повертає:
        str: Забарвлений ASCII-арт, який може бути виведений у консолі.
        Якщо сталася помилка, повертається None.

    Опис:
        Ця функція створює ASCII-арт із заданого тексту, застосовуючи зазначений шрифт та масштабуючи результат
        відповідно до вказаної ширини та висоти. Пробіли замінюються на вказаний символ. Колір арту встановлюється
        за допомогою colorama і використовує переданий параметр кольору.

    Використання:
        1. Використовувати будь-який текст, шрифт, колір та символ для створення кастомного ASCII-арту.
        2. Якщо вказано недійсне значення шрифта або кольору, буде виведено відповідну помилку.

    Приклад:
        generate_ascii_art("Hello", "slant", "red", 50, 10, "#")

    Викидає:
        pyfiglet.FontNotFound: Якщо вказаний шрифт не знайдено.
        Exception: Якщо виникає інша помилка при генеруванні ASCII-арту.
    """
    try:
        # Генерація ASCII-арту
        ascii_art = pyfiglet.figlet_format(text, font=font)
        
        # Масштабування арту відповідно до заданих ширини та висоти
        lines = ascii_art.split('\n')
        scaled_art = []

        for i in range(height):
            if i < len(lines):
                line = lines[i]
                line = line.replace(' ', symbol)  # Замінюємо пробіли на символ
                line = line[:width].ljust(width, symbol)  # Масштабуємо до потрібної ширини
            else:
                line = symbol * width  # Якщо висоти не вистачає, заповнюємо символами
            scaled_art.append(line)

        # Перетворення в одну строку
        ascii_art = '\n'.join(scaled_art)
        
    except pyfiglet.FontNotFound:
        print("Шрифт не знайдено. Будь ласка, виберіть інший шрифт.")
        return None
    except Exception as e:
        print(f"Помилка при створенні ASCII-арту: {e}")
        return None
    
    # Застосовуємо колір до ASCII-арту
    color_code = COLOR_MAP.get(color, Fore.WHITE)
    colored_art = f"{color_code}{ascii_art}{Style.RESET_ALL}"
    return colored_art
