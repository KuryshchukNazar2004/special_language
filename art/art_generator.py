from art.config import fonts, colors

def generate_ascii_art(text, symbol, width, height, color_choice, alignment):
    """
    Генерує ASCII-арт з тексту з можливістю вибору символу, кольору, вирівнювання та розмірів.

    Параметри:
    - text (str): Текст, який буде перетворений в ASCII-арт.
    - symbol (str): Символ, який використовується для заповнення пустих місць в ASCII-арті.
    - width (int): Ширина кожного символа в ASCII-арті.
    - height (int): Висота ASCII-арту.
    - color_choice (str): Колір для ASCII-арту (вибирається з наданого словника `colors`).
    - alignment (str): Вирівнювання тексту. Може бути 'center' (по центру) або 'right' (праворуч).

    Повертає:
    - (str): ASCII-арт у вигляді строки з кольоровим текстом.
    
    Викидає:
    - KeyError: Якщо вказаний колір або символ не знайдені в словниках `fonts` або `colors`.
    """

    # Створення пустих рядків для кожного рівня висоти ASCII-арту
    ascii_art_lines = ['' for _ in range(height)]
    
    # Перетворення кожного символу тексту на його ASCII-арт
    for char in text.upper():
        if char in fonts['standard']:
            char_lines = fonts['standard'][char]
            for i in range(height):
                if i < len(char_lines):
                    # Заміна символів на введений символ
                    ascii_art_lines[i] += char_lines[i].replace(char, symbol) + ' '
                else:
                    ascii_art_lines[i] += ' ' * (width + 1)  # Заповнюємо рядок пробілами

    # Отримуємо код кольору з вибраного кольору
    color_code = colors.get(color_choice, colors['black_and_white'])
    
    # Вирівнювання тексту
    if alignment == 'center':
        ascii_art_lines = [line.center(len(line) + (width * len(text))) for line in ascii_art_lines]
    elif alignment == 'right':
        ascii_art_lines = [line.rjust(len(line) + (width * len(text))) for line in ascii_art_lines]

    # Додаємо кольори до кожного рядка
    ascii_art_with_color = [color_code + line for line in ascii_art_lines]
    
    # Повертаємо згенерований ASCII-арт з кольорами
    return '\n'.join(ascii_art_with_color) + colors['black_and_white']
