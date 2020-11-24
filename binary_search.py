import random

answer = 3
list = [1, 2, 3, 4, 5]  

def average(num1, num2):
    return (num1 + num2) / 2

def binary_search(list, search_value):
    search_value = random.randint(1,10)
    highest_value = 10
    lowest_value = 1
    while True:
        if search_value == answer:
            print(f'Congratulations, you\'ve answered correctly! {search_value} is the answer!')
            break
        elif search_value < answer:
            previous_search_value = search_value
            search_value = int(average(search_value, highest_value) +1)
            highest_value = previous_search_value
            print(search_value)
        elif search_value > answer:
            previous_search_value = search_value
            search_value = int(average(search_value, lowest_value) -1)
            lowest_value = previous_search_value
            print(search_value)

binary_search(list, answer)
