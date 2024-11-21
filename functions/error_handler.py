def ConvertNumberType(nums):
    nums = nums.replace(',', '.')
    try:
        number = float(nums)
        if number.is_integer():
            return int(number)
        return number
    except ValueError:
        raise ValueError(f"Invalid number: '{nums}'")

def GetNumber():
    while True:
        num = input("Введіть число: ")
        try:
            if num == "":
                raise ValueError("Field cannot be empty. Please enter a valid number.")
            return num
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number.")
