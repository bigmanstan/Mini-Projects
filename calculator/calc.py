import SciCalc
def print_menu():
    print('*******')
    print("Calculator")
    print('*******')

    print('[1] Add')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')
    print('[5] Scientific Calculator Options')


    print('[x] Exit')

def clear():
    print('\n' * 50)
    # 50 lines distance to keep cli clean looking

opc = ''
error = True

while(opc != 'x' ):
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1' or opc == '2' or opc == '3' or opc == '4'):

        while(error):
            try:
                num1 = float(input("Input your first number "))
                error = False
            except:
                error = True
                print("That wasnt a valid number, try again\n")
        error = True
        while(error):
            try:
                num2 = float(input("Input your second number "))
                error = False
            except:
                error = True
                print("That wasnt a valid number, try again\n")

            
        if(opc == '4' and num2 == 0):
            while(num2 == 0):
                print("Error, can not divide by 0")
                num2 = float(input("Input your second number again"))
    
    if(opc == '1'):
        print(num1 + num2)
        input()
    elif(opc == '2'):
        print(num1 - num2)
        input()
    elif(opc == '3'):
        print(num1 * num2)
        input()
    elif(opc == '4'):
        print(num1 / num2)
        input()
    elif(opc == '5'):
        SciCalc.SciCal()
        print("over to scientific section")


    if(opc =='x'):
        input("Press Enter to Exit the Program")