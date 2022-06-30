import math


def jump_search(number, array):
    length = len(array)
    block_size = int(math.sqrt(length))
    block = block_size
    prev_block = 0
    if array[length - 1] < number:
        return -1
    while block <= length and array[block - 1] < number:
        prev_block = block
        block += block_size
    while array[prev_block] < number:
        prev_block += 1
        if prev_block == min(block, length):
            return -1
    if array[prev_block] == number:
        return prev_block
    return -1


print(jump_search(87, [2, 5, 7, 12, 33, 87, 216, 367]))