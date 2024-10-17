from art_generator import generate_ascii_art
from user_input import get_text_input, get_font_choice, get_color_choice
from file_manager import save_to_file
from preview import preview_art

def main():
    print("Ласкаво просимо до ASCII-ART генератора!")

    while True:
        # Введення користувача
        text = get_text_input()

        # Вибір шрифту
        font = get_font_choice()

        # Вибір кольору
        color = get_color_choice()

        # Генерація ASCII-арту
        ascii_art = generate_ascii_art(text, font, color)

        # Попередній перегляд
        preview_art(ascii_art)

        # Збереження у файл
        save_to_file(ascii_art)

        # Запит на продовження чи вихід
        continue_choice = input("Бажаєте продовжити? (так/ні): ").strip().lower()
        if continue_choice != 'так':
            print("Дякуємо за використання ASCII-ART генератора! До побачення!")
            break
