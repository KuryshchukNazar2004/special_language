def main():
    """
    Основна функція для запуску програми генерації ASCII-арту.
    
    Мета:
    1. Збирає ввід користувача (текст, символи, параметри розміру, колір, вирівнювання).
    2. Генерує ASCII-арт на основі введених параметрів.
    3. Виводить результат на екран.
    4. Запитує користувача, чи бажає він зберегти ASCII-арт у файл.
    5. Дає можливість користувачу продовжити або завершити роботу.

    Повертає:
    None

    Опис роботи:
    Функція викликає інші модулі для отримання вводу користувача, генерує ASCII-арт за допомогою функції `generate_ascii_art()`, виводить результат та пропонує зберегти арту в файл через функцію `save_to_file()`. Програма запитує, чи бажає користувач продовжити генерацію нових артів, поки користувач не вибере 'n' для виходу.

    Приклад виклику:
    - Викликається автоматично при запуску програми.
    """
    
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
