def max_sequence(arr):
    result = set([0])
    for i in range(len(arr)):
        for j in range(len(arr), i, -1):
            result.add(sum(arr[i:j]))

    return max(result)


test_arr = [6, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sequence(test_arr))
