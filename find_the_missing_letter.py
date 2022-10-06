def find_missing_letter(chars):
    o = [ord(x) for x in chars]
    for i in range(1, len(o)):
        if (o[i] - o[i - 1]) == 2:
            return chr(o[i] - 1)


l = ["a", "b", "c", "d", "f"]
l1 = ["O", "Q", "R", "S"]

print(find_missing_letter(l))
print(find_missing_letter(l1))
