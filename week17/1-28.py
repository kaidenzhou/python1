#Homework Q17
def factor(num):
    a_list=[]
    for n in range(1,num+1): #This check for the factors and if it doesn't factor then it leaves out that number
        x=num%(n)
        if x==0:
            a_list.append(n) 
    return a_list
test_number=1000
test_list=factor(test_number)

print("The factors for " + str(test_number) + " is " + str(test_list))

#Q17.2

def check_prime(num):
    is_prime=True
    if num==1: #Since the code below range is 2 i added this because 1 isn't a prime number
        is_prime=False
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    return is_prime

def prime_factors(num):
    a_list=[]
    for n in range(1,num+1): 
        x=num%(n)
        if x==0:
            if check_prime(n):
                a_list.append(n) 
    return a_list

test_prime_number=28
test_prime_list=prime_factors(test_prime_number)

print("The prime factors for " + str(test_prime_number) + " is " + str(test_prime_list))






