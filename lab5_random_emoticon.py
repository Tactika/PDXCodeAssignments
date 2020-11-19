# Damien Richcreek
# PDX Code Guild
# Evening Python Bootcamp

import random

eyes = [
    ':',
    ';',
    '8',
    'B',
] 

noses = [
    '-',
    '=',
    '^',
    '*',
]

mouths = [
    ')',
    '(',
    'P',
    '|',
]

def makeFace():
    '''Creates a single face using characters from the lists eyes, noses, and mouths.'''
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    
    face = eye + nose + mouth
    return face

def main():
    '''Creates multiple faces using the makeFace function'''
    face_count = 0
    faces = []
    while face_count < 5:
        faces.append(makeFace())
        face_count += 1
    print(faces)    

main()
