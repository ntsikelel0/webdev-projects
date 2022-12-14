#Ntsikei's Calculatopr

def addition(a,b):
    return a + b


def subtraction(a,b): #(9,9) (a=9, b=9)
    if(a < b):
        return b - a
    elif(a > b):
        return a - b
    else:
        return("There is no difference between the 2 numbers. Goodbye!")

def multiplication(a,b):
    return a * b

def division(a,b):
    if (b != 0):
        return a/b
    elif(b == 0):
        return("You can not divide by zero. Goodbye!")
    
num1 = int(input("Please enter the first number: "))
#if type(num1) != "<class 'int'>":
#    print("You have entered an invalid option. Goodbye!")
    
num2 = int(input("Please enter the second number: "))
#if type(num2) != "<class 'int'>":
#    print("You have entered an invalid option. Goodbye!")

option1 = input("Would you like to add the two numbers; Y or N ? ")
if (option1 == 'Y' or option1 == 'y'):
    print(addition(num1,num2))
elif(option1 == 'N' or option1 == 'n'):
    option2 = input("Would you then like to take the difference of the two numbers; Y or N ? ")
    if (option2 == 'Y' or option2 == 'y'):
        print(subtraction(num1,num2))
    elif(option2 == 'N' or option2 == 'n'):
        option3 = input("Would you then like to multiply the two numbers; Y or N ? ")
        if (option3 == 'Y' or option3 == 'y'):
            print(multiplication(num1,num2))
        elif(option3 == 'N' or option2 == 'n'):
            option3 = input("Would you then like to divide the two numbers; Y or N ? ")
            if (option3 == 'Y' or option3 == 'y'):
                print(division(num1,num2))
            elif(option3 == 'N' or option2 == 'n'):
                print("It seems you don't want to do any math today, Goodbye!")
            else:
                print("You have entered an invalid option. Goodbye!")
        else:
            print("You have entered an invalid option. Goodbye!")
    else:
        print("You have entered an invalid option. Goodbye!")
else:
    print("You have entered an invalid option. Goodbye!")




