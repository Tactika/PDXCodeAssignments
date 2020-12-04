
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
            return whole_tens[number]
        elif number in lower_num and number < 20:
            return lower_num[number]
        elif number > 21 and number < 100:
            ones_place = number % 10
            tens_place = number // 10
            return str(tens[tens_place] + lower_num[ones_place])
        elif number in whole_hundreds:
            return whole_hundreds[number]
        elif number >= 100 and number <= 999:
            hundreds = number // 100
            tens_place = (number % 100) // 10
            ones_place = (number % 100) % 10
            if number - (hundreds * 100)  in lower_num:
                teens = number - (hundreds * 100)
                return str(lower_num[hundreds] + ' hundred ' + lower_num[teens])
            elif number - (hundreds * 100) in whole_tens:
                tens_place = number - (hundreds * 100)
                return str(lower_num[hundreds] + ' hundred ' + whole_tens[tens_place])
            else:
                return str(lower_num[hundreds] + ' hundred ' + tens[tens_place] + lower_num[ones_place])
        else:
            break
    
for i in range(1000):
    num_to_phrase(i)


