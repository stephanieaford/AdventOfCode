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


def part_one():
    invalid_id_sum = 0
    for id_range in ranges:
        first_id, last_id = id_range.split('-')
        first = int(first_id)
        last = int(last_id)
        nums = [num for num in range(first, last + 1)]

        for num in nums:
            if not is_valid(str(num)):
                invalid_id_sum += num
    print(invalid_id_sum)


def part_two():
    pass


part_one()
