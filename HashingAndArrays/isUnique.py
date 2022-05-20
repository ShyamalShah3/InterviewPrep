MAX_CHAR = 128 # for typical ASCII string length - change for extended ASCII


# This code technically has O(1) time and space complexity since a maximum of 128/256 iterations will occur. More
# realistically, it takes O(min(c,n)) time complexity where c is the number of characters in the character set and n
# is the number of characters in the string, s. The space complexity is also O(min(c,n)).
# Could reduce space complexity by using a bit vector. If an additional data structure cannot be used, then the fastest
# to solve this problem would be by sorting the input string and then iterating through the sorted string: O(nlog(n)).
# Alternatively, the brute force approach would take O(n^2) time.
def is_unique(s: str):
    assert len(s) >= 0 # sanity check
    if len(s) > MAX_CHAR: return False # there must be duplicate character.
    if len(s) < 2: return True # there cannot be a duplicate character if the length is 1.
    hash_dict = {} 
    for char in s:
        if char in hash_dict: # if the character is already in the dictionary, it must be a duplicate. This check takes O(1) time.
            return False
        else:
            hash_dict[char] = 1 # adding character to hash map along with a dummy value of 1.
    return True # all characters in the string must be unique


