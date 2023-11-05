def largest_radial_sum(arr, d):
    n = len(arr) // d
    max_honor = float('-inf')

    for i in range(n):

        current_honor = 0

        for j in range(i, len(arr), n):
            current_honor += arr[j]

        max_honor = max(max_honor, current_honor)

    return max_honor


