import pyfiglet
from colorama import Fore, Style
import config

def generate_ascii_art(text, font, color):
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
    except pyfiglet.FontNotFound:
        print("Шрифт не знайдено. Будь ласка, виберіть інший шрифт.")
        return None
    except Exception as e:
        print(f"Помилка при створенні ASCII-арту: {e}")
        return None
    
    color_code = config.COLOR_MAP.get(color, Fore.WHITE)
    colored_art = f"{color_code}{ascii_art}{Style.RESET_ALL}"
    return colored_art
