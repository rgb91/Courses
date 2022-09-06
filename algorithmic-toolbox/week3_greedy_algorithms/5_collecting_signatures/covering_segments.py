from sys import stdin

def optimal_points(segments: list):
    points = []
    segments.sort(key=lambda x: x[1])
    ix = 0
    while ix < n:
        curr = segments[ix]
        while ix < n-1 and curr[1] >= segments[ix+1][0]:
            ix += 1
        points.append(curr[1])
        ix += 1
    return points


if __name__ == '__main__':
    in_data = stdin.read()
    # in_data = input()

    n, *data = map(int, in_data.split())
    data = list(zip(data[::2], data[1::2]))
    # print(data)
    points = optimal_points(data)
    print(len(points))
    print(*points)
