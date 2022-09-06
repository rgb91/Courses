"""
Works for only single digits
"""
def largest_number_naive(numbers: list):
    numbers.sort(reverse=True)
    numbers = list(map(str, numbers))
    return "".join(numbers)

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
