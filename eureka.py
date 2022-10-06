def sum_dig_pow(a, b):
    result = []
    for x in range(a, b + 1):
        l = [int(a) for a in list(str(x))]
        s = 0
        for i in range(len(l)):
            s += l[i] ** (i + 1)
        if s == x:
            result.append(x)

    return result
