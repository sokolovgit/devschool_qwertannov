def high_and_low(list):
    lst = [int(x) for x in list.split()]
    return str(f"{max(lst)} {min(lst)}")


print(high_and_low((input())))