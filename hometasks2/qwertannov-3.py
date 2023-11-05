def group_anagrams(arr):

    result = []

    while arr:
        word = arr.pop(0)
        temp_lst = [word]

        i = 0
        
        while i < len(arr):
            if len(word) == len(arr[i]) and set(word) == set(arr[i]):
                temp_lst.append(arr[i])
                arr.pop(i)
            else:
                i += 1

        result.append(temp_lst)

    return result


