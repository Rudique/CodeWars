def valid_parentheses(string):
    l = 0
    for letter in string:
        if letter == '(':
            l += 1
        elif letter == ')' and l > 0:
            l -= 1
        elif letter == ')' and l == 0:
            return False
    if l == 0:
        return True
    else:
        return False


print(valid_parentheses(""))
