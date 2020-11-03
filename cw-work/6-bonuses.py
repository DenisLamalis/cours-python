# Bonuses

def bonus(arr, s):

    total = 0
    result = []

    for number in arr:
        total = total + (1 / number)

    coef = s / total

    for number in arr:
        result.append(round(coef / number))

    return result


print(bonus([22, 3, 15], 18228))

# [22, 3, 15], 18228, [1860, 13640, 2728]

# def bonus(arr, s):
#     s=s/(sum(1/n for n in arr))
#     return [round(s/n) for n in arr]