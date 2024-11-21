import re

def get_user_input():
    while True:
        text = input("Введіть слово або фразу для ASCII-арту (латиницею): ").strip()
        
        if re.search('[А-Яа-я]', text):
            print("Будь ласка, напишіть на англійській мові.")
            continue  

        symbol = input("Введіть символ для заповнення (наприклад, '@', '#', '*'): ").strip()
        width = int(input("Введіть ширину ASCII-арту: "))
        height = int(input("Введіть висоту ASCII-арту: "))
        
        print("Доступні кольори: black_and_white, gray, red, green, yellow, blue, magenta, cyan, white")
        color_choice = input("Виберіть колір: ").strip()

        print("Виберіть вирівнювання (left, center, right):")
        alignment = input().strip().lower()
        
        # Перевірка на допустимі значення вирівнювання
        if alignment not in ['left', 'center', 'right']:
            print("Недійсне вирівнювання. Будь ласка, виберіть з 'left', 'center', 'right'.")
            continue

        return text, symbol, width, height, color_choice, alignment
