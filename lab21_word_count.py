# Lab 21 - Count Words

import string

# Book Setup
translator = str.maketrans('', '', string.punctuation)
s = open('alice.txt', encoding='utf-8')
contents = s.read()
new_contents = contents.translate(translator)
words = new_contents.lower().split()

def remove_stopwords(input_list: list)->list:
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
    'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", '“i']
    updated_list = []

    updated_list = [word for word in input_list if word not in stopwords]

    return updated_list

def count_words(word_list: list)->dict:
    word_count = {}
    for key in word_list:
        word_count[key] = word_list.count(key)
    return word_count

def top_ten(word_count_dict: dict)->dict:
    words = list(word_count_dict.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(words))):
        print(words[i])

def main(word_list: list)->dict:
    upd_words = remove_stopwords(words)
    word_count = count_words(upd_words)
    top_ten(word_count)

main(words)
