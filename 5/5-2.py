"""
Basic logic is to do stuff backwards. Start from the smallest location and check whether that is a
valid seed number. O(n) in time complexity and it fails as input > 10e9
"""

import typing


def find_backward(start, mappings) -> int:
    for mapping in reversed(mappings):
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
    return start


def pre_process(mapping):
    mapping.sort(key=lambda x: x[0])
    if mapping[0][0] != 0:
        mapping.insert(0, [0, 0, mapping[0][0]])
    mapping.append(
        [mapping[-1][0] + mapping[-1][2], mapping[-1][0] + mapping[-1][2], 10000]
    )
    return mapping


def is_valid_seed_number(number, seeds) -> bool:
    for i in range(0, len(seeds), 2):
        if number >= seeds[i] and number <= seeds[i] + seeds[i + 1]:
            return True
    return False


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
        mapping.append([int(n) for n in line.split(" ")])
    mappings.append(pre_process(mapping))

    n = 0
    while True:
        res = find_backward(n, mappings)
        if is_valid_seed_number(res, seeds):
            return n
        n += 1

if __name__ == "__main__":
    cards_raw = []
    with open("in", "r") as file:
        result = solve(file.readlines())
    print(result)
