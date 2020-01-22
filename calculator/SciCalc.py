import math
import calc

def print_menu():

    print('*******')
    print("Scientific Calculator")
    print('*******')

    print('[1] Inverse')
    print('[2] Square')
    print('[3] Cube')
    print('[4] Root')
    print('[5] Log base 10')
    print('[6] Log base 2')
    print('[x] Exit to Simple calculator')

def clear():
    print('\n' * 50)
    # 50 lines distance to keep cli clean looking


def SciCal():

    loop = True
    while(loop):

        print_menu()
        
        operator = input('Enter your option\n')
        if(operator == 'x'):
            loop = False
            calc.main()
            continue
        oprand = float(input("Enter input\n"))

        if(operator == '1'):
            print("Result : ",1/oprand)
            input()
            clear()
        elif(operator == '2'):
            print("Result : ",oprand**2)
            input()
            clear()

        elif(operator == '3'):
            print("Result : ",oprand**3)
            input()
            clear()
        elif(operator == '4'):
            print("Result : ",oprand**0.5)
            input()
            clear()
        else:
            print(" Invalid Input....Try again")
            input()
            clear()
        
        
def main():
    
    SciCal()

if __name__ == "__main__":
    SciCal()      