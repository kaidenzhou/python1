# Week 14 homework 
#Even or Odd
num= int(input("Please type a number: "))

if num % 2==0:
    print(num,"is an even number")

else:
    print(num,"is an odd number")

#Sum of Digits
number = int(input("Enter a Number: "))
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