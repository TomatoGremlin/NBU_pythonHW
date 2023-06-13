'''
Създайте програма, която отваря файл със stem (качен в Moodle) и ги вкарва в речник. Програмата с име FXXXXX_L10_T2.py, 
където XXXXX е вашият факултетен номер, 
да получава параметри от командния ред (със sys.argv, не от клавиатурата) име на stem файл и дума. 
След попълване на речника да се проверява получената като параметър дума за нейната основна форма 
и да се извежда резултата в стандартния изход.
'''
import sys

def create_word_stem_dictionary(input_file):
    word_stem_dict = {}
    
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            word, stem = line.split(':')
            word_stem_dict[word] = stem
    
    return word_stem_dict


input_file = sys.argv[1]
word = sys.argv[2]
word_stem_dictionary = create_word_stem_dictionary(input_file)

if word in word_stem_dictionary:
    print(word_stem_dictionary[word])


