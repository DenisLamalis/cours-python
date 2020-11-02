# Remove consecutive duplicate words

def remove_consecutive_duplicates(words):
    word_list = words.split(" ")
    index = 0

    for y in word_list:
        index = word_list.index(y, index)
        if index+2 > len(word_list):
            break
        if y == word_list[index+1]:
            del word_list[index+1]

    word_list = ' '.join(word_list)
    return word_list


print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))


# def remove_consecutive_duplicates(s):
#     s = s.split()
#     l = len(s)-1
#     while l > 0:
#         if s[l] == s[l-1]:
#             s.pop(l)
#         l -= 1
        
#     return ' '.join(s)


# from itertools import groupby

# def remove_consecutive_duplicates(s):
#     return ' '.join(k for k,_ in groupby(s.split()))

