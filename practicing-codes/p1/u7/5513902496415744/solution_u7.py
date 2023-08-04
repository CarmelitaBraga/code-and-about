def slicer(start, end, array):
    new_array = []
    for j in range(start, start + end):
        new_array.append(array[j])
    return new_array


def is_substring(word, seq):
    array_seq = []
    array_word = []
    array_seq += seq
    array_word += word
    for i_word in range((len(word) - len(seq)) + 1):
        interval = (slicer(i_word, len(seq), array_word))
        if array_seq == interval:
            return True
    return False
