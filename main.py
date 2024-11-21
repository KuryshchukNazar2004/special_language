from calculator import Calculator
from memory import Memory
from functions.menu import DisplayMenu
from functions.operations import MathOperation

def main():
    calc = Calculator()
    mem = Memory()

    while True:
        DisplayMenu()  
        choice = input("Select an operation (1-13): ")
        if not MathOperation(choice, calc, mem):
            break 

if __name__ == "__main__":
    main()
