"""
Checks to see if two strings are one(or zero) edit away from each other (insert, remove, replace)
"""


def one_away(a: str, b: str) -> bool:
    """

    :param a: First string
    :param b: Second String
    :return: True if a and b are one edit away from being equal. False otherwise
    This code has a runtime of O(n), where n is the length of the shorter string between a and b.
    """
    # leveraging the fact that insert is the inverse of remove
    if len(a) == len(b): return replace_check(a, b) # equal length, check to see if less than 1 replace is needed
    elif len(a) - 1 == len(b): return insert_check(a, b) # length diff of one, check to see if one insert away
    elif len(a) == len(b) - 1: return insert_check(b, a) # length diff of one, check to see if one insert away
    return False # length diff greater than one, so automatically false


def replace_check(a: str, b:str) -> bool:
    """

    :param a: First string
    :param b: Second String
    :return: True if a and b are <=1 replacement away from being equal. False Otherwise
    """
    count = 0  # count to keep track of replacements needed
    for i in range(len(a)):
        if a[i] != b[i]: count += 1 # replacement is needed
    return count < 2 # if more than 1 replacement needed, return False


def insert_check(base: str, to_insert: str) -> bool:
    """

    :param base: the base string. len(base) = len(to_insert) + 1
    :param to_insert: the string where a character could be inserted. len(to_insert) = len(base) - 1
    :return: True if a and b are 1 insert away from being equal. False otherwise
    """
    index1 = 0  # index to iterate through base
    index2 = 0  # index to iterate through to_insert
    while (index1 < len(base)) and (index2 < len(to_insert)):  # check so we don't go out of bounds
        if base[index1] != to_insert[index2]:  # char are not equal
            if index1 != index2: return False  # we have already inserted, so auto return false
            index1 += 1  # increase base index
        else:  # char equal, so increase both indexes
            index1 += 1
            index2 += 1
    return True  # must be true
