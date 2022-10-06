def snail(snail_map):
    result = []
    while len(snail_map) != 0:
        result += help_func(snail_map)
        snail_map = make_me_tiny(snail_map)

    return result


def make_me_tiny(map):
    if len(map) == 2:
        return []
    else:
        map_to_return = []
        for y in range(1, len(map) - 1):
            map_to_return.append([])
            for x in range(1, len(map) - 1):
                map_to_return[y - 1].append(map[y][x])
        return map_to_return


def help_func(tiny_snail_map):
    result = []
    if len(tiny_snail_map) == 1:
        return tiny_snail_map[0]
    else:
        x = 0
        y = 0
        dx = 1
        dy = 0

        for amount_of_elems in range(4 * (len(tiny_snail_map) - 1)):
            result.append(tiny_snail_map[y][x])

            test = x + dx if dx else y + dy

            if test < 0 or test == len(tiny_snail_map):
                dx, dy = -dy, dx

            x += dx
            y += dy

    return result


array = [[1,  2,   3,  4,  5],
         [6,  7,   8,  9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]


print(snail(array))
