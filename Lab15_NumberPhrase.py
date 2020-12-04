lower_num = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen', 
}

tens = {
    0: '',
    1: '',
    2: 'twenty-',
    3: 'thirty-',
    4: 'fourty-',
    5: 'fifty-',
    6: 'sixty-',
    7: 'seventy-',
    8: 'eighty-',
    9: 'ninety-',
}   
whole_tens = {
     10: 'ten',
     20: 'twenty',
     30: 'thirty',
     40: 'fourty',
     50: 'fifty',
     60: 'sixty',
     70: 'seventy',
     80: 'eighty',
     90: 'ninty'
 }
whole_hundreds = {
     100: 'One Hundred',
     200: 'Two Hundred',
     300: 'Three Hundred',
     400: 'Four Hundred',
     500: 'Five Hundred',
     600: 'Six Hundred',
     700: 'Seven Hundred',
     800: 'Eight Hundred',
     900: 'Nine Hundred',
 }

def num_to_phrase(number):
    while True:
        if number in whole_tens:
            print(f'{whole_tens[number]}')
            break
        elif number in lower_num and number < 20:
            print(f'{lower_num[number]}')
            break
        elif number > 21 and number < 100:
            ones_place = number % 10
            tens_place = number // 10
            print(f'{tens[tens_place]}{lower_num[ones_place]}')
            break
        elif number in whole_hundreds:
            print(f'{whole_hundreds[number]}')
            break
        elif number >= 100:
            hundreds = number // 100
            tens_place = (number % 100) // 10
            ones_place = (number % 100) % 10
            if number - (hundreds * 100)  in lower_num:
                teens = number - (hundreds * 100)
                print(f'{lower_num[hundreds]} hundred {lower_num[teens]}')
                break
            elif number - (hundreds * 100) in whole_tens:
                tens_place = number - (hundreds * 100)
                print(f'{lower_num[hundreds]} hundred {whole_tens[tens_place]}')
                break
            else:
                print(f'{lower_num[hundreds]} hundred {tens[tens_place]}{lower_num[ones_place]}')
                break
        else:
            print('Invalid Input')
            print(f'The number {number} is not in the range of 0 thru 999')
            break
    
num_to_phrase(0)
num_to_phrase(2)
num_to_phrase(3)
num_to_phrase(10)
num_to_phrase(12)
num_to_phrase(17)
num_to_phrase(27)
num_to_phrase(88)
num_to_phrase(99)
num_to_phrase(100)
num_to_phrase(380)
num_to_phrase(525)


