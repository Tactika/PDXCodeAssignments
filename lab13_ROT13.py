import string

string = input("Please enter the string you'd like to encrypt:  ")
rotations = int(input("How many rotations would you like to encrypt by?:  "))

alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punct = """!"#$%&'()*+,-./0123456789:;<=>?@"""

decoded_lower = [*range(97, 123)]
decoded_upper = [*range(65, 91)]
decoded_punct = [*range(33, 65)]


def encrypt_data(string, rotations):
    # characters = len(string)
    encoded_string = ""

    for letter in string:
        if letter not in alphabet_lower:
            new_letter = (ord(letter) + rotations - 97) % 26 + 97
            new_letter = chr(new_letter)
            encoded_string += new_letter
        elif letter in alphabet_upper:
            new_letter = (ord(letter) + rotations - 65) % 26 + 65
            new_letter = chr(new_letter)
            encoded_string += new_letter
        elif letter in punct:
            new_letter = (ord(letter) + rotations - 33) % 32 + 33
            new_letter = chr(new_letter)
            encoded_string += new_letter
        else:
            new_letter = " "
            encoded_string += new_letter

    print(encoded_string)


encrypt_data(string, rotations)
