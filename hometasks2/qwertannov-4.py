def is_sausage(s):
    if s[0] != '[' or s[-1] != ']' or len(s) != 6:
        return False
    s = s[1:5]
    is_all_the_same = all(char == s[0] for char in s)
    return is_all_the_same


def unpack_sausage_box(s):
    s = ' '.join(s[1:5])
    return s


def unpack_sausages(data):
    res = []
    skip_count = 0

    for row in data:
        for box in row:
            if is_sausage(box):
                if skip_count != 4:
                    res.append(unpack_sausage_box(box))
                skip_count = (skip_count + 1) % 5

    res = ' '.join(res)
    return res




