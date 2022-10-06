def make_readable(seconds):
    result = ''
    if len(str(seconds // 3600)) < 2:
        result += '0' + str(seconds // 3600) + ':'
    else:
        result += str(seconds // 3600) + ':'
    if len(str((seconds % 3600) // 60)) < 2:
        result += '0' + str(((seconds % 3600) // 60)) + ':'
    else:
        result += str((seconds % 3600) // 60) + ':'
    if len(str(seconds % 60)) < 2:
        result += '0' + str(seconds % 60)
    else:
        result += str(seconds % 60)
    return result


a = 0
print(make_readable(a))
