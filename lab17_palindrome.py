# Lab 17: Palindrome and Anagram

# Palindrome Checker

def rev_string(string:str) -> str:
    ''' Takes string and reverses the order of the letters'''
    reverse_string = ''
    for i in string:
        reverse_string = i + reverse_string
    return reverse_string

def check_palindrome(string:str) -> str:
    ''' Compares string to a reversed version of a string, returns True/False''' 
    reversed_string = rev_string(string)
    while reversed_string == string:
        return True
    else:
        return False

# Anagram Checker

def check_anagram(string_one:str, string_two:str) -> bool:
    string_one = sorted(string_one.lower().replace(' ', ''))
    string_two = sorted(string_two.lower().replace(' ', ''))

    while string_one == string_two:
        return True
    else:
        return False