from sys import stdin


def optimal_value(capacity, weights, values):
    total_value = 0
    items = [(v, w) for v, w in zip(values, weights)]
    items.sort(key=lambda x: x[0]/x[1], reverse=True)

    for v, w in items:
        if capacity == 0:
            return total_value
        amount = min(capacity, w)
        total_value = total_value + amount*(v/w)
        capacity = capacity - amount
    return total_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    # data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
