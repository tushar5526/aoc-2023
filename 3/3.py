SYMBOLS = set()


def is_valid_idx(x, y, width, height):
    return x < height and y < width and x >= 0 and y >= 0


def validate(x, y_start, y_end):
    width = len(engine[0])  # y
    height = len(engine)  # x

    valid_idxs = {(x, y_start - 1), (x, y_end + 1)}
    valid_idxs.update({(x - 1, y) for y in range(y_start - 1, y_end + 2)})
    valid_idxs.update({(x + 1, y) for y in range(y_start - 1, y_end + 2)})
    # print("indexes to be cheked", valid_idxs)

    for idx in valid_idxs:
        if is_valid_idx(*idx, width, height) and engine[idx[0]][idx[1]] in SYMBOLS:
            return True
    return False


def solve():
    width = len(engine[0])
    height = len(engine)
    s = 0
    for x in range(height):
        y_start = 0

        while y_start < width:
            if not engine[x][y_start].isdigit():
                y_start += 1
                continue

            y_end = y_start
            while y_end < width and engine[x][y_end].isdigit():
                y_end += 1

            y_end = max(y_start + 1, y_end)

            if validate(x, y_start, y_end - 1):
                s += int("".join([engine[x][j] for j in range(y_start, y_end)]))
            y_start = y_end

    return s


if __name__ == "__main__":
    engine = []
    with open("in", "r") as file:
        for line in file:
            for c in line:
                if c != "." and not c.isdigit() and c != '\n':
                    SYMBOLS.add(c)
            engine.append(list(line.strip()))
