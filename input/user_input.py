import pyfiglet
import re

def get_text_input():
    while True:
        text = input("Введіть слово або фразу для ASCII-арту: ")
        if re.search('[а-яА-ЯёЁіІїЇєЄ]', text):
            print("Будь ласка, введіть текст англійською мовою.")
        else:
            return text

def get_font_choice():
    available_fonts = ['standard', 'slant', 'block', 'bubble', 'big', 'electronic']  
    print("Доступні шрифти:", ", ".join(available_fonts))
    font = input("Виберіть шрифт з наведеного вище списку: ")
    if font not in available_fonts:
        print("Обраний шрифт недоступний. Використовується шрифт за замовчуванням: 'standard'.")
        return 'standard'
    return font

def get_color_choice():
    colors = ['red', 'green', 'blue', 'white']
    print("Доступні кольори:", ", ".join(colors))
    color = input("Виберіть колір: ").lower()
    if color not in colors:
        print("Невірний колір. Використовується колір за замовчуванням: 'white'.")
        return 'white'
    return color

def get_dimensions():
    width = int(input("Введіть ширину ASCII-арту (число більше 0): "))
    height = int(input("Введіть висоту ASCII-арту (число більше 0): "))
    return width, height

def get_symbol_choice():
    symbol = input("Введіть символ для заповнення (наприклад, '@', '#', '*'): ")
    return symbol
