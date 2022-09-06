def optimal_summands(n):
    if n<=1: return [1]
    summands = []
    num = n
    for i in range(1, n):
        if num > 2*i: 
            summands.append(i)
            num = num - i
        else:
            summands.append(num)
            break
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
