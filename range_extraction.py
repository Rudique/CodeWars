def solution(args):
    res = ''
    data = [args[0]]
    for i in range(1, len(args)):
        if args[i] - 1 == data[len(data) - 1]:
            data.append(args[i])
        elif args[i] - 1 != data[len(data) - 1] or i == len(args) - 1:
            if len(data) < 3:
                for elem in data:
                    res += str(elem) + ','
            else:
                res += str(data[0]) + '-' + str(data[len(data)-1]) + ','
            data = [args[i]]
    if len(data) < 3:
        for elem in data:
            res += str(elem) + ','
    else:
        res += str(data[0]) + '-' + str(data[len(data) - 1]) + ','
    return res[:-1]


test = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
print(solution(test))
