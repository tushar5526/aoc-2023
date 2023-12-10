"""
Solution is basically to solve
    t * (T - t) > D
    tT - t^2 > D
    t^2 -tT + D < 0
and then find the lower and upper bounds
"""
import typing
import math

def find_bound(T:int, D:int) -> typing.Tuple[int, int]:
    discriminant = T ** 2 - 4 * D
    assert discriminant >= 0, "discriminant is less than 0"
    # The lower and upper bounds are exclusive, so a small delta value is added here
    # to select the next int in the exclusive range
    lower = math.ceil((T - math.sqrt(discriminant)) / 2 + 0.0000001)
    upper = math.floor((T + math.sqrt(discriminant)) / 2 - 0.0000001)
    return lower, upper

def solve(times: list[int], distances: list[int]):
    ans = 1
    for time, distance in zip(times, distances):
        low, high = find_bound(time, distance)
        ans *= (high - low + 1)
    return ans

if __name__ == "__main__":
    cards_raw = []
    with open("in", "r") as file:
        times = [int(n) for n in file.readline().strip().split(':')[1].strip().split()]
        distance = [int(n) for n in file.readline().strip().split(':')[1].strip().split()]

    print(solve(times, distance))
