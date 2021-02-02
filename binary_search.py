import random

def average(num1, num2):
    return int((num1 + num2) / 2)

def binary_search(range_list, search_value):
    mid_index = average(0, len(range_list))
    highest_index = len(range_list) - 1
    lowest_index = 0
    while True:
        if search_value == mid_index:
            print('Correct')
            return search_value
        elif search_value > highest_index or search_value < lowest_index:
            print('Not in Range')
            return -1
        elif search_value < mid_index:
            previous_mid_index = mid_index
            mid_index = average(lowest_index, mid_index - 1)
            highest_index = previous_mid_index
        elif search_value > mid_index:
            previous_mid_index = mid_index
            mid_index = average(mid_index, highest_index + 1)
            lowest_index = previous_mid_index


binary_search([1,2,3,4,5], 4)
