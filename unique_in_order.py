def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    iterable = list(iterable)
    x = iterable[0]
    result = list()
    result.append(x)
    for elem in iterable:
        if elem != x:
            result.append(elem)
            x = elem

    return result


print(unique_in_order([1, 2, 2, 3, 3]))
