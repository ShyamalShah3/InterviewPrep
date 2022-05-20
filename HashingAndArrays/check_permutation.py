# Given two strings, check to see if the strings are permutations of each other


"""
This code runs in O(n) (linear) time. It also takes O(n) of space. We first save character counts for every character
in s1 in a hash map (python dictionary). Then we iterate through s2 and decrease character counts in the hash map. If a
character in s2 does not exist in s2, or if the character count in the hash map is less than 0, then we automatically
return false.
"""


def check_permutation(s1: str, s2: str):
    if len(s1) != len(s2): return False
    hash_map = {}
    for char in s1:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
    for char in s2:
        if char not in hash_map: return False
        else:
            hash_map[char] -= 1
            if hash_map[char] < 0: return False
    return True

