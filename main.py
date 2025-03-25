import CalculatorApp

def menu():
    print("A to add")
    print("S to subtract")
    print("D to divide")
    print("M to multiply")
    print("E to exit")
    selection = input("Enter your selection: ")
    while selection not in ('A','a','D','d','M','m','e','E','s','S'):
        print("Incorrect selection")
        selection = input("Enter your selection: ")
    return selection


print("Welcome to the ultimate calculator")

calc = CalculatorApp.Calculator()

print ("What do you want to do today:")
selection = menu()
while (selection != 'E'):
    first_num = int(input("Enter the first number: "))
    sec_num = int(input("Enter the second number: "))
    match selection:
        case 'a' | 'A':
            calc.add(first_num, sec_num)
        case 's' | 'S':
            calc.subtract(first_num, sec_num)
        case 'd' | 'D':
            calc.divide(first_num, sec_num)
        case 'm' | 'M':
            calc.multiply(first_num, sec_num)
    print()
    selection = menu()

print("Bye bye")






