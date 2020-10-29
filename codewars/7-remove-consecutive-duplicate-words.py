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
    list_length = len(word_list)
    print(list_length)

    # for x in range(list_length):
    #     print(x)
    #     if word_list[x] == word_list[x]:
    #         del word_list[1]
        
    #         if word_list[x] == word_list[x]:
    #             del word_list[1]

    print(word_list)


print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))

