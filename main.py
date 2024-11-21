from functions.classes.calculator import Calculator, Memory
from functions.functions.Menu import DisplayMenu 
from functions.functions.MathOperation import MathOperation

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
