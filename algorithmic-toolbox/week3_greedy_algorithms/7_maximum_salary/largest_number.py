def is_greater_or_equal(d1, d2):
    return int(str(d1)+str(d2))>=int(str(d2)+str(d1))

def largest_number_naive(numbers):
    largest = []
    while numbers:
        max_digit = 0
        for digit in numbers:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        largest.append(max_digit)
        numbers.remove(max_digit)
    return "".join(largest)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
