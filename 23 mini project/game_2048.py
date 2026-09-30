def compress(row):
    values = [n for n in row if n]
    result = []
    i = 0
    while i < len(values):
        if i + 1 < len(values) and values[i] == values[i + 1]:
            result.append(values[i] * 2)
            i += 2
        else:
            result.append(values[i])
            i += 1
    return result + [0] * (len(row) - len(result))

def move_left(board):
    return [compress(row) for row in board]

if __name__ == "__main__":
    board = [[2, 0, 2, 4], [4, 4, 0, 0], [2, 2, 2, 2], [0, 0, 0, 2]]
    for row in move_left(board):
        print(row)
