##
# Warren Kuang
# Course: CIS 117 PythonProgramming
# Lab #1: Arithmetic, Data Types, User Input, Importing Modules
# Application: Expression set calculations
# Description: Expression set of mixed data type operations.  
#              Import datetime module to obtain timestamp.
# Input: User input validated for lastname and student id.
# Requirements: Family name contains at least two letters.
#               College Student ID is a positive integer.
# Output: Expression results as per lab specification. 
# Development Environment: Ubuntu 17.0
# Version:  Python 3.7
# Solution File: CIS117_ExampleSolnLab1.py
# Date: 06/27/23

from datetime import date
def main ():

    family_name = input ("Enter your family name: ")
    num_let = len(family_name)

    #Initialize number of letters and numbers
    number_count = 0
    letter_count = 0 

    #Verify family name doesn't have numbers and >= 2 letters 
    for check in family_name:
        if (check <= 'z' and check >= 'a') or (check <= 'Z' and check >= 'A'):
            letter_count += 1
        else:
            number_count += 1
    if letter_count < 2 and letter_count > 15:
        print ("Invalid input. Family name should have more than 2 letters")
        return
    if number_count > 0:
        print ("Family name should only have letters.")
        return
           
    #user input of student ID as an int
    student_id = int(input("Enter your student ID: "))
    mod_student_id = str(student_id) #converts to str to be iterated

    #sum of all digits in student id
    my_id = 0
    for char in mod_student_id:
        new_char = int(char)
        my_id += new_char
    print ("my_id is: ", my_id)

    #print length of family name
    print("num_let is:", num_let)

    #expressions 1-9
    exp1 = my_id / 2
    exp2 = my_id % 2
    exp3 = 2
    if num_let == 2:
        exp3 += 2
    else:
        for i in range(3, num_let + 1):
            exp3 += i
    exp4 = my_id + num_let
    exp5 = abs(num_let - my_id)
    exp6 = (my_id) / (num_let + 1100)
    exp7 = num_let % num_let and my_id * my_id
    exp8 = 1 or my_id / 0
    exp9 = round(3.15,1)

    #printing expressions 1-9
    print("expression 1: ", "%.2f" %exp1)
    print("expression 2: ", "%.2f" %exp2)
    print("expression 3: ", exp3)
    print("expression 4: ", "%.2f" %exp4)
    print("expression 5: ", "%.2f" %exp5)
    print("expression 6: ", "%.2f" %exp6)
    print("expression 7: ", bool(exp7))
    print("expression 8: ", bool(exp8))
    print("expression 9: ", "%.2f" %exp9)
    
    print (date.today())

main()