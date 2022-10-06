def in_array(array1, array2):
    result = []
    for elem in array1:
        for el in array2:
            if elem in el and elem not in result:
                result.append(elem)
                break

    return sorted(result)


a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
