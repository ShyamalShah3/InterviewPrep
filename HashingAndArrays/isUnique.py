MAX_CHAR = 128 # for typical ASCII string length - change for extended ASCII


# This code technically has O(1) time and space complexity since a maximum of 128/256 iterations will occur. More
# realistically, it takes O(min(c,n)) time complexity where c is the number of characters in the character set and n
# is the number of characters in the string, s. The space complexity is also O(min(c,n)).
# Could reduce space complexity by using a bit vector. If an additional data structure cannot be used, then the fastest
# to solve this problem would be by sorting the input string and then iterating through the sorted string: O(nlog(n)).
# Alternatively, the brute force approach would take O(n^2) time.
def is_unique(s: str):
    assert len(s) >= 0
    if len(s) > MAX_CHAR: return False
    if len(s) < 2: return True
    hash_dict = {}
    for char in s:
        if char in hash_dict:
            return False
        else:
            hash_dict[char] = 1
    return True


