def slicer(i_start, i_end, sequence):
    new = ''
    for i in range(i_start, i_end):
        new += sequence[i]
    return new


def is_substring_expr(str1,str2):
    start, end = str2.split('*')
    s_len = len(start)
    e_len = len(end)
    if slicer(0, s_len, str1) == start and slicer(len(str1) - e_len, len(str1), str1) == end:
            return True
    return False
