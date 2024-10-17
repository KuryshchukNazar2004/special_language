import os
import re

def save_to_file(ascii_art):
    save_option = input("Чи хочете ви зберегти ASCII-арт у файл? (y/n): ").strip().lower()
    
    if save_option == 'y':
        file_name = input("Введіть назву файлу (без розширення): ")
        
        os.makedirs('txt_files', exist_ok=True) 
        
        with open(f"txt_files/{file_name}.txt", 'w', encoding='utf-8') as file:
            clean_ascii_art = re.sub(r'\x1b\[[0-?9;]*[mK]', '', ascii_art)
            file.write(clean_ascii_art)
        
        print(f"ASCII-арт збережено у файл txt_files/{file_name}.txt")
    else:
        print("ASCII-арт не збережено.")
