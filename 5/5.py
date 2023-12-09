import typing


def find_next(start, mappings) -> int:
    for mapping in mappings:
        i_start = start
        broke = False
        for idx in range(1, len(mapping)):
            curr = mapping[idx]
            prev = mapping[idx - 1]
            if start >= prev[0] and start < curr[0]:
                broke = True
                start += prev[1] - prev[0]
                break
        if not broke:
            start += mapping[-1][1] - mapping[-1][0]
    #     print(f"Moved {i_start} -> {start}")
    # print("==================")
    return start


def pre_process(mapping):
    mapping.sort(key=lambda x: x[0])
    if mapping[0][0] != 0:
        mapping.insert(0, [0, 0, mapping[0][0]])
    mapping.append(
        [mapping[-1][0] + mapping[-1][2], mapping[-1][0] + mapping[-1][2], 10000]
    )
    return mapping


def solve(raw_input: typing.List[str]):
    seeds = [int(n) for n in raw_input[0].strip().split(":")[1].strip().split(" ")]
    mappings = []
    mapping = []
    for line in raw_input[3:]:
        line = line.strip()
        if not line:
            continue
        if "to" in line:
            mappings.append(pre_process(mapping))
            mapping = []
            continue
        dest, source, length = [int(n) for n in line.split(" ")]
        mapping.append([source, dest, length])
    mappings.append(pre_process(mapping))
    print(mappings)

    n = None
    for i in range(0, 101):
        print(f"{i} -> {find_next(i, mappings)}")
    return n


if __name__ == "__main__":
    cards_raw = []
    with open("in", "r") as file:
        result = solve(file.readlines())
    print(result)
