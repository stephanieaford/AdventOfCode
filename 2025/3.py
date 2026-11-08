lines = open('day3.txt').readlines()
banks = [list(map(int, line.strip())) for line in lines]


def find_max_jolt_p1(bank) -> int:
    first = max(bank[:-1])
    second = max(bank[(bank.index(first) + 1):])
    return int(f"{first}{second}")


def find_max_jolt_p2(bank) -> int:
    def inner(start_idx: int, remaining: int) -> int:
        largest = 0
        largest_idx = 0
        for i in range(start_idx, len(bank) - remaining + 1):
            curr = int(bank[i])
            if curr > largest:
                largest = curr
                largest_idx = i
        if remaining > 1:
            return largest * 10 ** (remaining - 1) + inner(largest_idx + 1, remaining - 1)
        else:
            return largest
    return inner(0, 12)


def day_three():
    bank_sum_p1 = 0
    bank_sum_p2 = 0
    for bank in banks:
        bank_sum_p1 += find_max_jolt_p1(bank)
        bank_sum_p2 += find_max_jolt_p2(bank)
    print(f"Part 1: {bank_sum_p1}")
    print(f"Part 2: {bank_sum_p2}")


day_three()
