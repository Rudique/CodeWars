def digital_root(n):
    s = sum([int(x) for x in list(str(n))])
    if s > 9:
        s = digital_root(s)
    return s


print(digital_root(942))
