from sys import stdin


def min_refills(milage, stops):
    refills, fuel_in_tank, prev = 0, milage, 0
    for i in range(n_stops):
        curr, next = stops[i], stops[i+1]
        fuel_in_tank = fuel_in_tank - (curr-prev)
        fuel_needed = next-curr
        if fuel_needed > milage:
            return -1
        if fuel_needed > fuel_in_tank:
            refills += 1
            fuel_in_tank = milage
        prev = curr
    return refills


if __name__ == '__main__':
    d, m, n_stops, *stops = map(int, stdin.read().split())
    # d, m, n_stops, *stops = map(int, input().split())
    stops.append(d)
    print(min_refills(m, stops))
