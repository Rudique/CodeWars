def same_structure_as(original, other):
    if type(original) == type(other) == list:

        if len(original) != len(other):
            return False
        else:
            for i in range(len(original)):
                if type(original[i]) == type(other[i]) == list:
                    return same_structure_as(original[i], other[i])
                elif not isinstance(original[i], type(other[i])) and list in [type(original[i]), type(other[i])]:
                    return False

    elif not isinstance(original, type(other)) and list in [type(original), type(other)]:
        return False
    return True




    # if len(original) != len(other):
    #     return False
    # for i in range(len(original)):
    #     if not isinstance(original[i], type(other[i])):
    #         return False
    #     elif type(original[i]) == list:
    #         return same_structure_as(original[i], other[i])
    #
    # return True


a = [1, [1, 1]]
b = [2, [2, 2]]
c = [1, 1, 1]
d = [2, 2, 2]

print(same_structure_as(a, b))
print(same_structure_as(c, d))
