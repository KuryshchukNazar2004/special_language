import pyfiglet
from colorama import Fore, Style
from art.config import COLOR_MAP

def generate_ascii_art(text, font, color, width, height, symbol):
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        
        lines = ascii_art.split('\n')
        scaled_art = []

        for i in range(height):
            if i < len(lines):
                line = lines[i]
                line = line.replace(' ', symbol)  
                line = line[:width].ljust(width, symbol)  
            else:
                line = symbol * width  
            scaled_art.append(line)

        ascii_art = '\n'.join(scaled_art)
        
    except pyfiglet.FontNotFound:
        print("Шрифт не знайдено. Будь ласка, виберіть інший шрифт.")
        return None
    except Exception as e:
        print(f"Помилка при створенні ASCII-арту: {e}")
        return None
    
    color_code = COLOR_MAP.get(color, Fore.WHITE)
    colored_art = f"{color_code}{ascii_art}{Style.RESET_ALL}"
    return colored_art
