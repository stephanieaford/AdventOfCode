lines = open('day3.txt').readlines()
banks = [list(map(int, line.strip())) for line in lines]


def find_max_jolt_p1(bank):
    first = max(bank[:-1])
    second = max(bank[(bank.index(first) + 1):])
    return int(f"{first}{second}")


def find_max_jolt_p2(bank):
    pass


def day_three():
    bank_sum = 0
    for bank in banks:
        bank_sum += find_max_jolt_p1(bank)
    print(f"Part 1: {bank_sum}")


day_three()
