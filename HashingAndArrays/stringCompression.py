"""
Method to perform basic String compression using the counts of repeated characters. If the compressed string is
not smaller than the original string, we return the original string
"""


def string_compression(s: str) -> str:
    """

    :param s: The string to compress
    :return: The compressed string if it is smaller than s. Otherwise, s.
    The time complexity of this code is O(n) where n is the length of s.
    """
    if len(s) < 3: return s  # if len(s) < 3, the compressed string will not be smaller than s
    ch = s[0]  # current char
    count = 1  # current char count
    compressed = [ch]  # keep track of current char and count

    for i in range(1, len(s)):  # loop through s
        if ch == s[i]:  # increase count if next char == ch
            count += 1
        else:  # new char
            compressed.append(str(count))  # append count of last char
            ch = s[i]  # update current char
            compressed.append(ch)  # append new char to compressed
            count = 1  # reset current char count
        if len(compressed) >= len(s): return s  # optimization
    compressed.append(str(count))  # append final count
    if len(compressed) >= len(s): return s  # if original string is same length or shorter, return original string
    return "".join(compressed)  # return compressed String
