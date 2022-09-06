if __name__ == '__main__':
    fib_list = [0, 1]
    for i in range(2, 46):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    n = int(input())
    print(fib_list[n])