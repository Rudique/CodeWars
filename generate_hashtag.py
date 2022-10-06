def generate_hashtag(s):
    a = list(s)
    result = '#'
    for i in range(len(a)):
        if i < len(a) - 1 and a[i] == ' ' and a[i + 1] != ' ':
            a[i + 1] = a[i + 1].upper()
        if i < len(a) - 1 and a[i] != ' ' and a[i + 1] != ' ':
            a[i + 1] = a[i + 1].lower()

        result += a[i]

    return result.replace(' ', '')


c = "    heLlo     WorlD   "
print(generate_hashtag(c))
