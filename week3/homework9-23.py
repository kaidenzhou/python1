def sum_list(a_list):
    total=0
    for number in a_list:
        total+=number
    return total
my_list = [1, 2, 3, 4, 5]
result = sum_list(my_list)
print(f"The sum of the list {my_list} is: {result}")