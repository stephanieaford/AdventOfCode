file = open('day4.txt')
diag = [line.strip() for line in file]
rows = len(diag)
cols = len(diag[0])


def neighbors(i: int, j: int) -> int:
    count = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (x, y) == (i, j):
                continue
            if x < 0 or x > rows - 1:
                continue
            if y < 0 or y > cols - 1:
                continue
            if diag[x][y] == '@':
                count += 1
    return count


def part_one():
    sum = 0
    for i in range(rows):
        for j in range(cols):
            if diag[i][j] != '@':
                continue
            if neighbors(i, j) < 4:
                sum += 1
    print(f"Part 1: {sum}")


part_one()
