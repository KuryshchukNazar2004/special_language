from art.config import fonts, colors

def generate_ascii_art(text, symbol, width, height, color_choice, alignment):
    ascii_art_lines = ['' for _ in range(height)]
    
    for char in text.upper():
        if char in fonts['standard']:
            char_lines = fonts['standard'][char]
            for i in range(height):
                if i < len(char_lines):
                    # Заміна символів на введений символ
                    ascii_art_lines[i] += char_lines[i].replace(char, symbol) + ' '
                else:
                    ascii_art_lines[i] += ' ' * (width + 1)  # Заповнюємо рядок пробілами

    color_code = colors.get(color_choice, colors['black_and_white'])
    
    # Вирівнювання тексту
    if alignment == 'center':
        ascii_art_lines = [line.center(len(line) + (width * len(text))) for line in ascii_art_lines]
    elif alignment == 'right':
        ascii_art_lines = [line.rjust(len(line) + (width * len(text))) for line in ascii_art_lines]

    # Додаємо кольори до кожного рядка
    ascii_art_with_color = [color_code + line for line in ascii_art_lines]
    return '\n'.join(ascii_art_with_color) + colors['black_and_white']
