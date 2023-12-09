import typing


def find_next(pairs, idx, mappings) -> int:
    """
    Recursive logic to break the input into smaller pairs and then send them over to the next
    mapping till we reach the location mapping
    :param pairs:
    :param idx:
    :param mappings:
    :return: int
    """
    if idx == len(mappings):
        return min(pairs, key=lambda x: x[0])[0]
    new_pairs = []
    for pair in pairs:
        start, end = pair

        for id, mapping in enumerate(mappings[idx]):
            source, dest, length = mapping
            if id == len(mappings[idx]) - 1:
                # Last Mapping getting checked
                # Quick fix, as length is taken max as 10e3 but this fails for actual output
                length = end + 1
            if start > source + length or end < source:
                # print("No overlap")
                # no overlap
                continue
            delta = dest - source
            if start >= source and end > source + length:
                # start point lies in segment
                # print("start point lies in segment")
                # print("adding ", (start + delta, min(source + length, end) + delta))
                new_pairs.append((start + delta, min(source + length, end) + delta))
            if start < source and end <= source + length:
                # end lies in segment
                # print("end lies in segment")
                # print("adding ", (source + delta, min(end, source + length) + delta))
                new_pairs.append((source + delta, min(end, source + length) + delta))
            if start < source and end > source + length:
                # print("Complete overlap, greater than")
                # print("adding ", (source + delta, source + length + delta))
                new_pairs.append((source + delta, source + length + delta))
            if start >= source and end <= source + length:
                # print("Complete overlap less than")
                # print("adding ", (start + delta, end + delta))
                new_pairs.append((start + delta, end + delta))


    # print("Pairs being created", new_pairs, "from ", pairs, "\n")
    return find_next(new_pairs, idx + 1, mappings)

def pre_process(mapping):
    mapping.sort(key=lambda x: x[0])
    if mapping[0][0] != 0:
        mapping.insert(0, [0, 0, mapping[0][0]])
    mapping.append(
        [mapping[-1][0] + mapping[-1][2], mapping[-1][0] + mapping[-1][2], 10000]
        # 10000 - this should be MAX_INT, but I don't know what is MAX_INT in python :p
        # This is fixed with a small "if" hack later
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

    n = None
    for i in range(0, len(seeds), 2):
        res = find_next([(seeds[i], seeds[i] + seeds[i + 1])], 0, mappings)
        n = min(n, res) if n else res
    return n


if __name__ == "__main__":
    cards_raw = []
    with open("in", "r") as file:
        result = solve(file.readlines())
    print(result)
