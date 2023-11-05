def find_even_index(arr):

    result = -1

    for i in range(len(arr)):
        if sum(arr[:i:]) == sum(arr[i+1::]):
            result = i
            break

    return result


