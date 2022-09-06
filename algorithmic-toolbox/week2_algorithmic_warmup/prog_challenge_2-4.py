def gcd(a: int, b: int) -> int:
    a, b = max(a,b), min(a,b)
    while a % b != 0:
        a, b = b, a%b
    return b

def lcm(a: int, b: int) -> int:
    return a*b//gcd(a, b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))