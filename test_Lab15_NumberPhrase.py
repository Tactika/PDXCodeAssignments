from Lab15_NumberPhrase import num_to_phrase


def test_num_to_phrase():
    assert num_to_phrase(0) == 'zero'
    assert num_to_phrase(13) == 'thirteen'
    assert num_to_phrase(50) == 'fifty'
    assert num_to_phrase(101) == 'one hundred one'
    assert num_to_phrase(723) == 'seven hundred twenty-three'
    assert num_to_phrase(999) == 'nine hundred ninety-nine'
