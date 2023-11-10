import re
import os

def calculator(num1, num2, oper):#calculate
    if oper == '+':
        answer = num1 + num2
        print(str(num1) + "+"+str(num2) + "=" + str(answer))
    elif oper == '-':
        answer = num1 - num2
        print(str(num1) + "-" + str(num2) + "=" + str(answer))
    elif oper == '*' or oper == 'x':
        answer = num1 * num2
        print(str(num1) + "*" + str(num2) + "=" + str(answer))
    elif oper == '/':
        if(num2 == 0):   #I put the check before division operation. please see this again.
            raise Exception(str(num1)+" can't be divided by 0.")
        print(str(num1) + "/" + str(num2) + "=" + str(answer))
    elif oper == '%':
        answer = num1 % num2
        print(str(num1) + "%" + str(num2) + "=" + str(answer))
    elif oper == '^':
        answer = num1 ** num2
        print(str(num1) + "^" + str(num2) + "=" + str(answer))
    return answer
    
def seperater(equation):
    #distinguish number and operator

    #This code means if the equation include the character which is not digit and operator, the code judge it's invalid.
    i = 0
    for i in range (0, len(equation)):
        if equation[i] in ('+', '-', '*', 'x', '/', '%', '^'):
            break;
        elif not equation[i].isdigit():
            raise Exception('The equation format is invalid.')
        

    #if there is no operator, raise exception
    #if there is no operator, the i will be end of array. The second if means there is no operator. Should I add more exception?
    if i == len(equation) - 1:
        raise Exception('The equation format is invalid.')

    num1, num2 = equation.split(equation[i])    
    oper = equation[i]                       #operator

    #check the numbers are valid
    if (num1.isdigit() or num2.isdigit()):
        num1 = int(num1)
        num2 = int(num2)
    else:
        raise Exception("The number is not digit")
    
    return num1, num2, oper
    
file = None
equation = None
while True:
    option = int( input("Please enter an option. (1: enter an calculation, 2: read from a file, 3: exit): "))

    if option == 1 :
        equation = input("please enter your equation in the format of 'number operator number'ex)4+1: ")

        num1, num2, oper = seperater(equation)
        answer = calculator(num1, num2, oper)



    elif option == 2:
        fileName = input("please enter your file name: ")    #request file name
        if fileName[-4:] != ".txt":     #if user doesn't enter .txt, put .txt
            fileName = fileName + ".txt"

        try:
            while os.path.isfile(fileName):
                readFile = input(fileName + "is already exist. Would you like to read the file? (yes/no)")
                if readFile == "yes":
                    file.open(fileName, 'r')
                    break
                elif readFile == "No":
                    overWrite = input("Would you like to overwrite?(yes/no)")
                    if overWrite == "Yes":
                        file.open(fileName, 'w')
                        break
                    elif overWrite == "No":
                        fileName = input("please enter another file name: ")

            file = open(fileName, 'w')     #if the specified file does not exist, create a file
            user_input = input("please enter an equation in the format of 'number operator number'ex)4+1 : ")
            file.write(user_input)
            equation = user_input
    
        except Exception:
            print("The file that you are trying to open can not be opened.")

        num1, num2, oper = seperater(equation)
        answer = calculator(num1, num2, oper)

        file = open(fileName,'a')
        file.write('\n' + str(num1) + oper + str(num2) + '=' + str(answer))
        file.close()

    elif option == 3:
        print("Thank you for using calculator.")
        break