# Remove consecutive duplicate words

def remove_consecutive_duplicates(words):
    # transformer words en liste
    # regarder word 1 + 2
    # sont-ils égaux ?
    # si oui delete le word 2
    #   regarder word 1 + 2
    #   ...
    # si non regarder word 2 + 3
    word_list = words.split(" ")

    for x in range(len(word_list)):
        print(word_list[x])
        
        if word_list[x] == word_list[x]:
            del word_list[x]
            x = x - 1
        
        #     if word_list[x] == word_list[x]:
        #         del word_list[x]

    print(word_list)


print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))

