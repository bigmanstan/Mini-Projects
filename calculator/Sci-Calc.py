import math

class SciCal():
    print('[1] Inverse')
    print('[2] Square')
    print('[3] Cube')
    print('[4] Root')
    print('[5] Log base 10')
    print('[6] Log base 2')

    operator = input('Enter your option\n')



    oprand = float(input("Enter input\n"))


    if(operator == '1'):
        print("Result : ",1/oprand)
    elif(operator == '2'):
        print("Result : ",oprand**2)
    elif(operator == '3'):
        print("Result : ",oprand**3)
    elif(operator == '4'):
        print("Result : ",oprand**0.5)
    else:
        print(" Invalid Input....Try again")
        SciCal
        
    
    
        