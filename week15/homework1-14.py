#Week 15 homework

#Odd or even
def odd_even(num):

    if num % 2==0:
        print(num,"is an even number")

    else:
        print(num,"is an odd number")


num= int(input("Please type a number: "))
odd_even(num)

#Sum of Digits
def sum_of_digit(number):
   
    sum_of_digits = 0
    #Loop through all digits in the interger. 
    while number != 0:
        #Get the right most digit using modulo operator
        last_digit = number % 10
        #Add the right most digit
        sum_of_digits = sum_of_digits + last_digit 
         #Use the floor division to get the other digit accept the right most one
        number = number // 10
    
    print("Sum of digits of a Number is: ", sum_of_digits)

#Take user input
myinput = input("Enter a Number: ")

if myinput.isnumeric():
    myNumber = int(myinput)
    sum_of_digit(myNumber)
else:
    print(f"{myinput} is not a number")    