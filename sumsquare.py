def sum_of_squares(numbers):
    odd_sum = 0
    even_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_sum+=number**2
        else:
             odd_sum+=number**2
    return [odd_sum,even_sum]
print(sum_of_squares([1, 2, 3, 4, 5])) 
