from lab17_palindrome import check_palindrome, check_anagram

def test_palindrome():
    assert check_palindrome('minim') == True
    assert check_palindrome('radar') == True
    assert check_palindrome('string') == False
    assert check_palindrome('malayalam') == True
    assert check_palindrome('aibohphobia') == True
    assert check_palindrome('default') == False

def test_anagram():
    assert check_anagram('anagram', 'nag a ram') == True
    assert check_anagram('study', 'dusty') == True
    assert check_anagram('bad credit', 'debit card') == True
    assert check_anagram('right answer', 'incorrect') == False
