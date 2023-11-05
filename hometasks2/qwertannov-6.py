def land_perimeter(arr):
    total_perimeter = 0
    rows, cols = len(arr), len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 'X':
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                perimeter = 4

                for ni, nj in neighbors:
                    if 0 <= ni < rows and 0 <= nj < cols and arr[ni][nj] == 'X':
                        perimeter -= 1

                total_perimeter += perimeter

    return f"Total land perimeter: {total_perimeter}"
