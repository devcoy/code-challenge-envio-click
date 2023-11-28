import re

def remove_special_chars(string):
    return re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚ]', '', string)

print('What word do you need search?')
word_to_search = input().strip()
with open('input_01.txt','r') as input_file:
    print('Word to search: ', word_to_search)
    count = 0;
    for text_line in input_file:
        for word in text_line.strip().split():
            word_sanitized = remove_special_chars(word)
            if word_sanitized == word_to_search:
                count+= 1
    input_file.close()
    print(f'The word has {count} matched.')
