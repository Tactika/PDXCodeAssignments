# Lab 21 - Count Words

import string

def book_setup(book_name: str)->str:
    s = open(book_name, encoding='utf-8')
    contents = s.read()

    return contents

def sentance_count(text_document: str)->int:
    statements = text_document.count('.')
    questions = text_document.count('?')
    exclamations = text_document.count('!')

    sentances = statements + questions + exclamations
    return sentances

def word_count(text_document: str)->int:
    num_words = len(text_document.lower().split())
    return num_words

def char_count(text_document: str)->int:
    characters = len(text_document)
    return characters

def compute_score(text_document: str)->int:
    characters = char_count(text_document)
    num_words = word_count(text_document)
    sentances = sentance_count(text_document)
    ari_score = round(4.17 * (characters / num_words) + 0.5 * (num_words / sentances) - 21.43)
    return ari_score

def main()->str: 
    book_name = input('What is the name of the text file you\'d like to grade?: ')
    text_document = book_setup(book_name)
    ari_scale = {
        1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
        2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
        3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
        4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
        5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
        6: {'ages': '10-11', 'grade_level':    '5th Grade'},
        7: {'ages': '11-12', 'grade_level':    '6th Grade'},
        8: {'ages': '12-13', 'grade_level':    '7th Grade'},
        9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }
    score = compute_score(text_document)
    score_dict = ari_scale[score]

    print(f'''
    -------------------------------------------------------------------------------
        
        The ARI for {book_name} is {score}
        This corresponds to a {score_dict['grade_level']} of difficulty
        that is suitable for an average person {score_dict['ages']} years old.

    -------------------------------------------------------------------------------
                
'''
    )

if __name__ == '__main__':
    main()