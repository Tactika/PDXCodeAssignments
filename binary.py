import random


def average(num1, num2):
    return int((num1 + num2) / 2)


def binary_search(range_list, search_value):
    mid_index = average(0, len(range_list))
    print(f'Mid Index:  {mid_index}')
    highest_index = len(range_list)
    print(f'High Index: {highest_index}')
    lowest_index = 0
    while True:
        if search_value not in range(lowest_index, highest_index):
            return -1
        elif mid_index == search_value:
            print(f'You are correct {search_value} is the search_value!')
            return range_list.index(mid_index)
        elif mid_index < lowest_index  mid_index > highest_index:
            print(f'Test Failed: {mid_index}')
            return -1
        elif mid_index > search_value:
            previous_mid_index = mid_index
            mid_index = average(mid_index, highest_index)
            highest_index = previous_mid_index
            print(f'Too Low: {mid_index}')
        elif mid_index < search_value:
            previous_mid_index = mid_index
            mid_index = average(mid_index, lowest_index)
            lowest_index = previous_mid_index
            print(f'Too High: {mid_index}')


binary_search([1, 2, 3, 4, 5], -1)
