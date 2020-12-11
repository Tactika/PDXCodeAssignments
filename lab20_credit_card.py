# Lab 20 Credit Card Validation

credit_card_str = '4556737586899855'

def multiply(credit_card_num: list)->list:
        for digit in range(len(credit_card_num)):
            if digit % 2 == 0:
                credit_card_num[digit] = credit_card_num[digit] * 2  
        return credit_card_num

def subtract(credit_card_num: list)->list:
        for digit in range(len(credit_card_num)):
             if credit_card_num[digit] > 9:
                 credit_card_num[digit] = credit_card_num[digit] - 9
        return credit_card_num

def validate(credit_card_str: str) ->bool:
    # converts str -> list:ints
    credit_card_num = list(map(int, credit_card_str))
    # slice last digit - (check digit)
    check_digit = credit_card_num.pop(-1)
    # reverse the digits
    credit_card_num = credit_card_num[::-1]
    # subtract 9 from digits over 9
    credit_card_num = multiply(credit_card_num)
    credit_card_num = subtract(credit_card_num)
    # sums all values
    credit_card_num = sum(credit_card_num)
    # takes 2nd digit of the sum
    credit_card_num = credit_card_num % 10
    conf_num = int(str(credit_card_num))
    #if 2nd digit == check digit print true
    if check_digit == conf_num:
        return True
    else:
        return False

validate(credit_card_str)