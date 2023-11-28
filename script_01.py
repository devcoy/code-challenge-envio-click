print('What word that you need search?')
word_to_search = input()
with open('input_01.txt','r') as input_file:
    print('Word to search: ', word_to_search)
    for text_line in input_file:
        print(text_line.strip())
