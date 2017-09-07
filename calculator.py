import sys


math_oper=input("What mathematical operation you want to use? ")

if (math_oper=="addition" or math_oper=="substraction" or math_oper=="multiplication" or math_oper=="division" ):
    try:
        first_number=input('What is the first number? ')
        first_number=int(first_number)
    
    except ValueError:
            print("This is not a number")
           
    try:
        second_number=input('What is the second number? ')
        second_number=int(second_number)
        
    except ValueError:
            print("This is not a number")
            sys.exit()
  
    if math_oper=="addition":
        print('The sum of the numbers is:',(first_number+second_number))
    if math_oper=="substraction":
        print('The substraction of the numbers is:',(first_number-second_number))
    if math_oper=="multiplication":
        print('The multiplication of the numbers is:',(first_number*second_number))
    if math_oper=="division":
        print('The division of the numbers is:',(first_number/second_number))

else:
    print("Operation doesn't exist")
    sys.exit()
    



