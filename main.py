from art.art_generator import generate_ascii_art
from input.user_input import (
    get_text_input, 
    get_font_choice, 
    get_color_choice, 
    get_dimensions,
    get_symbol_choice
)
from file.file_manager import save_to_file
from art.preview import preview_art

def main():
    print("Ласкаво просимо до ASCII-ART генератора!")

    while True:
        text = get_text_input()

        symbol = get_symbol_choice()

        width, height = get_dimensions()

        font = get_font_choice()

        color = get_color_choice()

        ascii_art = generate_ascii_art(text, font, color, width, height, symbol)

        preview_art(ascii_art)

        save_to_file(ascii_art)

        continue_choice = input("Бажаєте продовжити? (так/ні): ").strip().lower()
        if continue_choice != 'так':
            print("Дякуємо за використання ASCII-ART генератора! До побачення!")
            break

if __name__ == "__main__":
    main()