# Duane Anthony
# phase 1 of calculation library
# 2023-09-17
# expect to use parms eventually, but for now it is configured interactively for a user

import string

#def main(operation, type1, op1, op2):  -- possible future use as input parms
def main():

    cont = 'y'
    while(cont.lower() == 'y' ):

        # get operation & ensure it is a valid type
        operation = input("What operation would you like? (A)dd/(S)ubtract/(M)ultiply/(D)ivide: ").lower()
        while (operation not in ('a','s','m','d')):
            operation = input("Please enter a valid operation (a/s/m/d): ").lower()

        # get data type and ensure it is valid    
        type1 = input("What data type are your operands? (I)nteger/(F)loat/(S)cientific/(E)ngineering/(B)inary/(O)ctal/(H)ex: ").lower()
        while(type1 not in ('i','f','s','e','b','o','h')):
            type1 = input("Please enter a valid type. (I)nteger/(F)loat/(S)cientific/(E)ngineering/(B)inary/(O)ctal/(H)ex: ").lower()

        # Possible future - add output type rather than using the same one

        # get operands and ensure they are valid for the type
        check = True
        while check:
            op1 = input("Operand 1: ")
            op2 = input("Operand 2: ")

            try:
                match type1:
                    case 'i':
                        #integer
                        op1=int(op1)
                        op2=int(op2)
                        result = 0
                    case 'f':
                        #float
                        op1=float(op1)
                        op2=float(op2)
                        result = 0.0
                    case 's':
                        #scientific
                        op1=float(op1)
                        op2=float(op2)
                        result = 0.0E0
                    case 'e':
                        #engineering
                        op1=float(op1)
                        op2=float(op2)
                        result = 0.0E0    
                    case 'b':
                        #binary
                        op1=int(op1, 2)
                        op2=int(op2, 2)
                        result = 0
                    case 'o':
                        #octal
                        op1=int(op1, 8)
                        op2=int(op2, 8)
                        result = 0
                    case 'h':
                        #hex
                        op1=int(op1, 16)
                        op2=int(op2, 16)
                        result = 0
                check = False
            except ValueError:
                print("Operands do not match specified type of", type1, ".  Try Again") 

        # perform the math            
        match operation:
            case 'a': result = add(op1, op2)
            case 's': result = subtract(op1, op2)
            case 'm': result = multiply(op1, op2)
            case 'd':
                if(op2 != 0):
                    result = divide(op1, op2)
                    if(type1 in ('b','o','h')):
                       # non base-10 results must be integer 
                       result=round(result)
                else:
                    print("cannot divide by zero")
            case _: print("unsupported operation")

        # adjust output back to specified type
        match type1:
            case 'i': #integer
                    x = 0 # nothing needed
            case 'f': #float
                    x = 0 # nothing needed
            case 's': #scientific
                    result = "{:E}".format(result)
            case 'e': #engineering
                    result = engr_notation(result)
            case 'b': #binary
                    result = bin(result)
            case 'o': #octal
                    result = oct(result)
            case 'h': #hex
                    result = hex(result)

        #return(result)
        print(result)

        cont=input("Do another? (y/n) ")


def add(op1, op2):
    return(op1 + op2)  
    
def subtract(op1, op2):
    return(op1 - op2)

def multiply(op1, op2):
    return(op1 * op2)

def divide(op1, op2):
    # we already checked for the divide by zero issue
    return(op1 / op2)

def engr_notation(value):

    sci = "{:E}".format(value)
    num1 = float(sci.split("E")[0])
    exp = sci.split("E")[1]
    rem = int(exp)%3 # divisible by 3 ?
    match rem:
        case 0:
            new_exp   = int(exp)
            new_value = num1
        case 1:
            new_exp   = int(exp) - 1
            new_value = num1 * 10
        case 2:
            new_exp   = int(exp) - 2
            new_value = num1 * 100

    new_value = round(new_value,4)
    return(str(new_value) + "E" + str(new_exp))   


main()
