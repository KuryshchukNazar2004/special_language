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
    """
    Основна функція для генерації та збереження ASCII-арту.

    Опис:
        Ця функція є основним циклом програми, де користувач може ввести текст, 
        вибрати шрифт, колір, розміри та символи для генерації ASCII-арту.
        Після цього ASCII-арт буде згенеровано, відображено попередній перегляд та збережено у файл.

    Кроки виконання:
        - Запит користувача на введення тексту.
        - Запит користувача на вибір шрифта, кольору, розміру та символа.
        - Генерація ASCII-арту.
        - Виведення попереднього перегляду ASCII-арту.
        - Збереження ASCII-арту у файл.
        - Пропозиція продовжити або завершити роботу програми.

    Викидає:
        - ValueError або інші помилки, якщо функції для введення не виконуються належним чином.
    """
    print("Ласкаво просимо до ASCII-ART генератора!")

    while True:
        # Отримуємо текст для генерації ASCII-арту
        text = get_text_input()

        # Отримуємо символ для заповнення
        symbol = get_symbol_choice()

        # Отримуємо розміри ASCII-арту
        width, height = get_dimensions()

        # Отримуємо вибір шрифта
        font = get_font_choice()

        # Отримуємо вибір кольору
        color = get_color_choice()

        # Генеруємо ASCII-арт
        ascii_art = generate_ascii_art(text, font, color, width, height, symbol)

        # Показуємо попередній перегляд
        preview_art(ascii_art)

        # Зберігаємо в файл
        save_to_file(ascii_art)

        # Запит на продовження чи вихід
        continue_choice = input("Бажаєте продовжити? (так/ні): ").strip().lower()
        if continue_choice != 'так':
            print("Дякуємо за використання ASCII-ART генератора! До побачення!")
            break

if __name__ == "__main__":
    main()
