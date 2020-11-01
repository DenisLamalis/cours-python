# Bonuses

def bonus(arr, s):

    total = 0
    result = []

    for number in arr:
        total = total + (1 / number)

    coef = s / total

    for number in arr:
        result.append(int(coef / number))

    print(sum(result))

    return result


print(bonus([22, 3, 15], 18228))

# [22, 3, 15], 18228, [1860, 13640, 2728]