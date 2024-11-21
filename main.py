def main():
    from input.user_input import get_user_input
    from art.art_generator import generate_ascii_art
    from file.file_manager import save_to_file

    while True:
        # Отримуємо ввід від користувача
        text, symbol, width, height, color_choice, alignment = get_user_input() 
        
        # Генеруємо ASCII-арт
        ascii_art = generate_ascii_art(text, symbol, width, height, color_choice, alignment)
        print(ascii_art)
        
        # Запитуємо, чи зберегти ASCII-арт у файл
        save_to_file(ascii_art)  

        # Запит на продовження
        continue_option = input("Бажаєте продовжити? (y/n): ").strip().lower()
        if continue_option != 'y':
            print("Дякуємо за використання програми!")
            break

if __name__ == "__main__":
    main()
