
def to_camel_case(text):
    text = list(text)

    result = ''
    for i in range(len(text)):
        
        if text[i] in ["-", "_"] and i < len(text) - 1:
            text[i + 1] = text[i + 1].upper()

        if text[i] not in ["-", "_"]:
            result += text[i]
    return result


print(to_camel_case("the_stealth_warrior"))
