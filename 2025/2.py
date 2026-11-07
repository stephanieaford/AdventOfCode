file = open('day2.txt').read()
ranges = file.strip().split(',')


def is_valid(product_id: str) -> bool:
    if product_id[0] == '0':
        return False
    if len(product_id) % 2 == 1:
        return True
    length = len(product_id)
    first_half = product_id[:(length // 2)]
    second_half = product_id[(length // 2):]
    if first_half == second_half:
        return False
    return True


def is_valid_p2(product_id: str) -> bool:
    if not is_valid(product_id):
        return False
    for i in range(1, len(product_id)):
        if (len(product_id) % 1 == 0
                and product_id[:i] * (len(product_id) // i) == product_id):
            return False
    return True


def day_two():
    invalid_sum_p1 = 0
    invalid_sum_p2 = 0
    for id_range in ranges:
        first_id, last_id = id_range.split('-')
        first = int(first_id)
        last = int(last_id)
        nums = [num for num in range(first, last + 1)]

        for num in nums:
            if not is_valid(str(num)):
                invalid_sum_p1 += num
            if not is_valid_p2(str(num)):
                invalid_sum_p2 += num
    print(f"Part 1: {invalid_sum_p1}")
    print(f"Part 2: {invalid_sum_p2}")


day_two()
