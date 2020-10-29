# Remove consecutive duplicate words

def remove_consecutive_duplicates(words):
    word_list = words.split(" ")

    for y in word_list:
        index = word_list.index(y)
        print("y: ",y,"y+1: ",word_list[index+1])
        if y == word_list[index+1]:
            del word_list[index+1]

    for z in word_list:
        index = word_list.index(z)
        print("z: ",z,"z+1: ",word_list[index+1])
        if z == word_list[index+1]:
            del word_list[index+1]

    print(word_list)


print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))

