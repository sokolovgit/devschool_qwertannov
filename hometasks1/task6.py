def max_rearranged(string):
    lst = [int(x) for x in list(string)]
    lst.sort(reverse=True)
    return ''.join(map(str, lst))


print(max_rearranged(input()))

