def sum_list(a_list):

    result=0
    for num in a_list:
        result+=num
    return result
number_list=[1,3,-6,.5]

def average_list(a_list):
    average = sum(a_list) / len(a_list)
    return average
numbers = [1, 2, 3, 4, 5]
result = average_list(numbers)

if result is not None:
    print("Average:", result)
else:
    print("The list is empty.")


    