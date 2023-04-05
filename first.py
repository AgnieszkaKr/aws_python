import time
#a string is in single or double quotes
# new line \n

#string multiplication and addition
# print("Ha"*4)
# print("Ha"+"Ha")
#comment
"""
multiple
lines 
comment
"""

if False:
    print("False")
else:
    print("Yes")


#user input

# name=input("What is your name: ")
#print(f"Hello {name}")

#Function declaration

def hello_world():
    print("Hello world")

# hello_world()

def bmi_counter():
    weight=input("How much do you weight in kg? ")
    height=input("How tall are you in cm? ")
    height = int(height)/100
    bmi = int(weight)/ height**2
    if bmi< 18.5:
        print(f"Your BMI is {bmi}. You are in underweight range")
    elif bmi>= 18.5 and bmi< 24.9:
        print(f"Your BMI is {bmi}. You are in healthy weight range.")
    else:
        print(f"Your BMI is {bmi}. You are in obese range.")



# bmi_counter()
# now = time.localtime()

######################################### WORKING WITH FILES ############################################################
# open file you want to wrok with (read mode)
open_file = open("namex.txt", "r")
# print(open_file.read())
# return to the position at the top of document so I can print it twice
open_file.seek(0)
# print(open_file.read())
#if I don't need to make any changes I need to close file
# open_file.close()

# I can read or write files or do both at the same time "r+"
    # create a new file
    # open it for reading and writing
    # copy content from opened file
    # add a new line at the end 
    # print content

new_file = open("new_names.txt", "w")
new_file = open("new_names.txt", "r+")

new_file.write(open_file.read())
new_file.read()
new_file.write("\n6. Agnes")
new_file.seek(0)
# print(new_file.read())

######################################### WORKING WITH FILES ############################################################
import sys
# print first argument
# print(f"First argument {sys.argv[0]}")

import argparse

parser = argparse.ArgumentParser(description="Read files and reserve it.")

# added add_argument()
parser.add_argument("filename", help="File name ")
parser.add_argument("--limit", "-l", type=int, help="the numbers of line to read")
parser.add_argument("--version", "-v", action='version' ,version="%(prog)s 1.0")

args = parser.parse_args()
try:
    f= open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    # exit status eecho $? will return 2 if there is an error (exit function is from sys module)
    sys.exit(2)
else:
    # open file 
    with open(args.filename) as f:
        # take lines
        lines = f.readlines()
        # reverse the order of the lines
        lines.reverse()

        # check if we have limits
        if args.limit:
            lines = lines[:limit]

        # loop over lines and reverse lines
        for line in lines:
            print(line.strip()[::-1])