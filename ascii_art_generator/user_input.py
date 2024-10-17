import pyfiglet

def get_text_input():
    return input("Введіть слово або фразу для ASCII-арту: ")

def get_font_choice():
    fonts = pyfiglet.FigletFont.getFonts()
    print("Доступні шрифти:", fonts)
    font = input("Виберіть шрифт з наведеного вище списку: ")
    if font not in fonts:
        print("Обраний шрифт недоступний. Використовується шрифт за замовчуванням: 'standard'.")
        return 'standard'
    return font

def get_color_choice():
    colors = ['red', 'green', 'blue']
    print("Доступні кольори:", ", ".join(colors))
    color = input("Виберіть колір: ").lower()
    if color not in colors:
        print("Невірний колір. Використовується колір за замовчуванням: 'white'.")
        return 'white'
    return color
