#!/venv/bin/python3
"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits."""

def plusOne(digits: list[int]) -> list[int]:
    str_digits = ""

    for i in digits:
        str_digits += str(i)

    large_int = int(str_digits) + 1

    large_int_list = list(str(large_int))

    return [int(x) for x in large_int_list]

print(plusOne([9,9]))




""" Failed solution

digits[-1] = digits[-1] + 1
    dig_string = str(digits[-1])

    if len(dig_string) > 1:
        garbage = digits.pop()

        for i in dig_string:
            digits.append(int(i))
    
    return digits

print(plusOne([9, 9]))"""
