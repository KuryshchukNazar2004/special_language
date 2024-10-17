import os

def save_to_file(ascii_art):
    if ascii_art is None:
        print("Неможливо зберегти ASCII-арт, оскільки його не вдалося створити.")
        return

    # Видаляємо кольорові коди перед збереженням
    plain_ascii_art = ascii_art.replace("\033[31m", "").replace("\033[32m", "").replace("\033[34m", "").replace("\033[0m", "")

    # Створення папки, якщо її не існує
    if not os.path.exists('txt_files'):
        os.makedirs('txt_files')

    file_name = input("Введіть назву файлу для збереження (з розширенням .txt): ")
    file_path = os.path.join('txt_files', file_name)  # Шлях до файлу

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            # Зберігаємо ASCII-арт без кольорових кодів для файлу
            file.write(plain_ascii_art)
        print(f"ASCII-арт збережено у файл: {file_path}")
    except Exception as e:
        print(f"Помилка при збереженні файлу: {e}")
