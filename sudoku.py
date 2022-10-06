def sudoku(puzzle):

    while True:
        flag = True
        for i in range(9):
            for j in range(9):

                if puzzle[i][j] == 0:
                    flag = False
                    finder = [k for k in range(1, 10)]
                    to_remove = set(get_raw((i, j), puzzle) + get_col((i, j), puzzle) + get_block((i, j), puzzle))

                    for elem in to_remove:
                        if elem in finder:
                            finder.remove(elem)

                    if len(finder) == 1:
                        puzzle[i][j] = finder[0]
        if flag:
            return puzzle


def get_raw(pos, work_list):
    return work_list[pos[0]]


def get_col(pos, work_list) -> list:
    return [work_list[i][pos[1]] for i in range(9)]


def get_block(pos, work_list) -> list:
    rb = 3 + 3 * (pos[1] // 3)
    cb = 3 + 3 * (pos[0] // 3)
    return [work_list[i][j] for i in range(cb - 3, cb) for j in range(rb - 3, rb)]


puzzle_test = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]


for el in sudoku(puzzle_test):
    print(el)
