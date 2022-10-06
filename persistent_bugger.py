def persistence(n):
    count = 0
    if n < 10:
        return count
    else:
        l = [int(x) for x in list(str(n))]
        while len(l) != 1:

            n = 1
            count += 1
            for elem in l:
                n *= elem
            l = [int(x) for x in list(str(n))]

    return count


print(persistence(999))
