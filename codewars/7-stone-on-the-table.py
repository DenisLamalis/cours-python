# Stone on the table


def solution(stones):

    length = len(stones)-1
    number = 0

    for x in range(length):
        if stones[x] == stones[x+1]:
            number = number + 1
    return number


print(solution('RGGRGBBRGRR'))

# def solution(s):
#     return sum(1 for i in range(len(s)) if i and s[i-1]==s[i])