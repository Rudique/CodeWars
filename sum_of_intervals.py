def sum_of_intervals(intervals):
    result = []

    for elem in intervals:
        result += list(range(elem[0], elem[1]))

    return len(set(result))


print(sum_of_intervals([[1, 4], [7, 10], [3, 5]]))
