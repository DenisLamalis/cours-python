# Remove consecutive duplicate words

def remove_consecutive_duplicates(words):
    word_list = words.split(" ")
    index = 0

    for y in word_list:
        index = word_list.index(y, index)
        if y == word_list[index+1]:
            del word_list[index+1]

    word_list = ' '.join(word_list)
    return word_list


print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))

