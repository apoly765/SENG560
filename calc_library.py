# Duane Anthony
# phase 1 of calculation library
# 2023-09-17
# expect to use parms eventually, but for now it is configured interactively for a user

import string


#def main(operation, type1, op1, op2):  -- possible future use as input parms
def domath(operation,type1,op1,op2):
    

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

        return(result)
        

        


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



