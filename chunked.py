def chunked(lst, num):
    data = lst.split()
    if num >= len(data):
        return [data]
    result = []
    temp = []
    counter = num
    i = 0
    while i < len(data):
        if len(data) - i == 1:
            result.append([data[-1]])
            break
        while counter:
            temp.append(data[i])
            counter -= 1
            i += 1
        result.append(temp)
        temp = []
        counter = num
    return result


print(chunked(input(), int(input())))