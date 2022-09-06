# def last_digit_fibonacci_partial_sum(m: int, n: int) -> int:
#     if n<=1: return n
#     n = (n+2)%60
#     m = (m+1)%60
#     prev, curr, sum = 0, 1, 0
#     for i in range(2, n+1):
#         prev, curr = curr, (prev+curr) % 10
#         if i>=m: sum = (sum+curr) % 10
#         print(i, curr, sum)
#     return sum

# if __name__ == '__main__':
#     m, n = map(int, input().split())
#     print(last_digit_fibonacci_partial_sum(m, n))

# Python3
m, n = [int(i) for i in input().split()]

if n<=1:
    print(n)  
    quit()


lesser_n = (n+2)%60
lesser_m = (m+1)%60


def fibo(n):
    a,b = 0, 1
    for i in range(2,n+1):
        c = a+b
        c = c%10
        b, a = c, b
    return (c-1)
if lesser_n<=1:
    a = lesser_n-1
else:
    a = fibo(lesser_n)
if lesser_m<=1:
    b = lesser_m-1
else:
    b = fibo(lesser_m)
# print(a)
# print(b)
if a>=b:
    print(a-b)
else:
    print(10+a-b)