def ConvertNumberType(nums):
    """
    Перетворює рядок, що представляє число, в відповідний тип (int або float).
    Замінює коми на крапки перед конвертацією та обробляє значення, які можна перевести в ціле число.

    Параметри:
        nums (str): Рядок, який містить число, яке потрібно конвертувати.

    Повертає:
        int або float: Якщо число є цілим, повертається ціле число (int), в іншому випадку - число з плаваючою точкою (float).

    Викидає:
        ValueError: Якщо вхідне значення не є числом.

    Приклад:
        ConvertNumberType('10,5')  # Поверне 10.5 (тип float)
        ConvertNumberType('10')     # Поверне 10 (тип int)
        ConvertNumberType('10.0')   # Поверне 10 (тип int)
        ConvertNumberType('invalid') # Підніме ValueError
    """
    nums = nums.replace(',', '.')
    try:
        number = float(nums)
        if number.is_integer():
            return int(number)
        return number
    except ValueError:
        raise ValueError(f"Invalid number: '{nums}'")
