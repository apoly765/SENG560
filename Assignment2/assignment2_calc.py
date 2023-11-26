# Duane Anthony
#
# WVU SENG 560 Software Reuse
#
# 2023-11-18
#
# Assignment 2 - Reuse Calculator

# import code from muppalVT
from GIT_muppalVT.src.reuse_math.Operation import *


# this function provides a basic calculator
def calc():

    data_type = 0
    while data_type not in ('b', 'o', 'd', 'h'):
        data_type = input("What data type would you like (<b>in/<o>ct/<d>ec/<h>ex)? ")

    smart_calc = []
    while len(smart_calc) != 3:
        smart_cal = input("Enter your basic calculation (ie. 8 + 5), separated by spaces: ")
        smart_calc = smart_cal.split(" ")

    op1 = smart_calc[0] # get operand one
    sign = smart_calc[1] # get the sign
    op2 = smart_calc[2] # get operand two
    
    print(op1, sign, op2)
    print("=")
  
    match data_type:
        case 'd': #decimal
            match sign:
                case '+': #add
                    result = Operation([op1,op2]).add().as_int()
                case '-': #subtract
                    result = Operation([op1,op2]).subtract().as_int()
                case '*': #multiply
                    result = Operation([op1,op2]).multiply().as_int()
                case 'x': #multiply
                    result = Operation([op1,op2]).multiply().as_int()
                case '/': #divide
                    result = Operation([op1,op2]).divide().as_int()
        case 'b': #binary
            op1 = int(op1, 2)  # convert from binary
            op2 = int(op2, 2)
            match sign:
                case '+': #add
                    result = Operation([op1,op2]).add().as_bin()
                case '-': #subtract
                    result = Operation([op1,op2]).subtract().as_bin()
                case '*' : #multiply
                    result = Operation([op1,op2]).multiply().as_bin()
                case 'x' : #multiply
                    result = Operation([op1,op2]).multiply().as_bin()                    
                case '/': #divide
                    result = Operation([op1,op2]).divide().as_bin()
        case 'o': #octal
            op1 = int(op1, 8) # convert from octal
            op2 = int(op2, 8)
            match sign:
                case '+': #add
                    result = Operation([op1,op2]).add().as_oct()
                case '-': #subtract
                    result = Operation([op1,op2]).subtract().as_oct()
                case '*': #multiply
                    result = Operation([op1,op2]).multiply().as_oct()
                case 'x': #multiply
                    result = Operation([op1,op2]).multiply().as_oct()
                case '/': #divide
                    result = Operation([op1,op2]).divide().as_oct()
        case 'h': #hex
            op1 = int(op1, 16) # convert from hex
            op2 = int(op2, 16)
            match sign:
                case '+': #add
                    result = Operation([op1,op2]).add().as_hex()
                case '-': #subtract
                    result = Operation([op1,op2]).subtract().as_hex()
                case '*': #multiply
                    result = Operation([op1,op2]).multiply().as_hex()
                case 'x': #multiply
                    result = Operation([op1,op2]).multiply().as_hex()    
                case '/': #divide
                    result = Operation([op1,op2]).divide().as_hex()

    print(result)        

def display_table():
    # only add and multiply make sense
    print("This will generate a math table")
    x = input("Which operation would you like (<a>dd/<m>ultiply/)? ")
    match x:
        case 'a': #add
            for i in range(0,13):
                for j in range(0,13):
                    print(Operation([i,j]).add().as_int(),"\t",end="")
                print()
        case 'm': #multiply
            for i in range(1,13):
                for j in range(1,13):
                    print(Operation([i,j]).multiply().as_int(),"\t",end="")
                print()

def main():

    print("hello & welcome to a reuse calculator")

    cont = True
    while cont:

        print("Menu")
        print("  1) Calculator")
        print("  2) Display Practice Tables")
        sel = 0
        while sel not in ('1', '2'):
            sel = input("  Option?: ")

        if sel == "1":
            calc()
        else:      
            display_table()

        y = input("Want to do more <y>/<n>? ")
        if y[0].lower() != "y":
            cont = False

main()
