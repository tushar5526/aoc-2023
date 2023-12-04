from collections import defaultdict

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

digit_map_f = defaultdict(list)
digit_map_r = defaultdict(list)

[digit_map_r[d[-1]].append(d[::-1]) for d in digits]
[digit_map_f[d[0]].append(d) for d in digits]

for key in digit_map_f:
    digit_map_f[key].sort(key=len)
for key in digit_map_r:
    digit_map_r[key].sort(key=len)

digit_to_int_map_f = {digits[i]: str(i + 1) for i in range(len(digits))}
digit_to_int_map_r = {digits[i][::-1]: str(i + 1) for i in range(len(digits))}

def find_from_start(text):
    for i, c in enumerate(text):
        if c.isdigit():
            return i, c
        for d_a in digit_map_f[c]:
            if i + len(d_a) >= len(text):
                break
            if text[i:i + len(d_a)] == d_a:
                return i, digit_to_int_map_f[d_a]

def find_from_end(text):
    text = text[::-1]
    for i, c in enumerate(text):
        if c.isdigit():
            return i, c
        for d_a in digit_map_r[c]:
            if i + len(d_a) >= len(text):
                break
            if text[i:i + len(d_a)] == d_a:
                return i, digit_to_int_map_r[d_a]

def solve(input):
    s = 0

    for text in input:
        n = ''
        n += find_from_start(text)[1]
        n += find_from_end(text)[1]
        s += int(n)

    return s

if __name__ == "__main__":
    with open('in', 'r') as file:
        res = solve([line.strip() for line in file.readlines()])
        print("Answer is ", res)