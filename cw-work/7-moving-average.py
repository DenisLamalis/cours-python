# Moving Average

def moving_average(values,n):
   
    ws = n
    value = values
    sum = 0
    length = len(value)
    loop = 0
    result = []
    rank = 0
    
    while length >= ws:
        length = length - 1
        loop = loop + 1

    if ws == 0 or length < ws:
        return None

    for x in range(loop):

        for y in range(ws):
            z = y + rank
            sum = sum + value[z]
            
        rank = rank + 1
        sum = sum / ws
        result.append(sum)
        sum = 0

    return result



print(moving_average([40, 30, 50, 46, 39, 44], 7))

    # def moving_average(a, n):
    #   if 0 < n <= len(a): return [sum(a[i:i+n]) / n for i in range(len(a) - n + 1)]
    
    # def moving_average(arr, n):
    #   return n and [sum(arr[i:i + n]) / n for i in range(len(arr) - n + 1)] or None