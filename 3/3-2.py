from functools import reduce

def is_valid_idx(x, y):
    return x < height and y < width and x >= 0 and y >= 0

def search_number(x, y, check_prev=False):
    if not is_valid_idx(x, y):
        return False, None
    if not engine[x][y].isdigit():
        return False, None
    if check_prev and engine[x][y - 1].isdigit():
        return False, None
    y_start = y_end = y
    while y_start >= 0 and engine[x][y_start].isdigit():
        y_start -= 1
    while y_end < width and engine[x][y_end].isdigit():
        y_end += 1
    return True, int(''.join(engine[x][y_start + 1:y_end]))

def solve():
    s = 0
    indexes = [(-1, -1, False), (-1, 0, True), (-1, 1, True), (1, -1, False), (1, 0, True), (1, 1, True),
               (0, -1, False), (0, 1, False)]
    for i in range(height):
        for j in range(width):
            numbers = []
            if engine[i][j] == '*':
                for dx, dy, check in indexes:
                    valid, number = search_number(i + dx, j + dy, check)
                    if valid: numbers.append(number)

            if len(numbers) < 2:
                continue
            print(f"Found Numbers ({', '.join([str(n) for n in numbers])}) for ({i}, {j})")
            s += reduce(lambda x, y: x * y, numbers, 1)
    return s


if __name__ == "__main__":
    engine = []
    with open("in", "r") as file:
        for line in file:
            engine.append(list(line.strip()))
    width, height = len(engine[0]), len(engine)
    print(solve())
