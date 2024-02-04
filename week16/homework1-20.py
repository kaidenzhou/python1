#Week 16 homework

#Odd or even
def is_even(num):

    if num % 2==0:
        #print(num,"is an even number")
        return True
    else:
        #print(num,"is an odd number")
        return False
#Get the sum of intergers from 1 to input number    
def sum_of_all_even_numbers(interger):
    
    #Use interger as input number
    total=0

    #Loop through all number from 1-interger
    for number in range(1,interger+1):
        #Within the loop found if number is odd or even
        if(is_even(number)):
            #If it's a even number add it to the total    
            total+=number
    print(total)
sum_of_all_even_numbers(100)


