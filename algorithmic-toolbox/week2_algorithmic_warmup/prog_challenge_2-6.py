# Calculate and return Pisano Period
# The length of a Pisano Period for
# a given m ranges from 3 to m * m
def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
         
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

def last_digit_fibonacci_sum(n: int) -> int:
    if n<=1: return n
    n = n % 60
    if n<=1: return n
    prev, curr, sum = 0, 1, 1
    for _ in range(n-1):
        prev, curr = curr, (prev+curr) % 10
        sum = (sum + curr) % 10
    return sum

if __name__ == '__main__':
    n = int(input())
    print(last_digit_fibonacci_sum(n))