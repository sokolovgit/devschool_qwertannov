def find_nb(m):
    n = 0
    sum = 0
    while True:
        n += 1
        sum += n ** 3
        if sum > m:
            return -1
        elif sum == m:
            return n


print(find_nb(int(input())))

