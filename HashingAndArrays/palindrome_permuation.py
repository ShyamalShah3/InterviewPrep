# checks to see if a permutation of a given input string is a palindrome. We only account for non-letter characters.

import string


def lower_letter(s: str) -> str:
    """
    Time Complexity - O(n), where n is the length of the input string
    Space Complexity - O(n), where n is the length of the input string
    :param s: Input String
    :return: Permutation of input string such that all non-letters have been removed and all letters are in lowercase.
    """
    letter_set = frozenset(string.ascii_lowercase + string.ascii_uppercase)  # immutable set of all ascii letters
    filtered = []
    for ch in s: # filter out all non-letters
        if ch in letter_set:
            filtered.append(ch)
    return ''.join(filtered).lower()  # converts result to lowercase


def palindrome_permutation(s: str) -> bool:
    """
    Time Complexity - O(n), where n is the length of the input string.
    Space Complexity - O(n), where n is the length of the input string.
    :param s: Input String
    :return: Boolean value indicating if a permutation of the input string is a palindrome
    """
    if len(s) <= 1: return True
    lowercase = lower_letter(s)  # remove all non-letters and convert to lowercase
    is_odd = (len(lowercase) % 2) == 1  # odd/even number of letters in input string
    hash_map = {}  # to store counts of characters
    odd_counter = 0  # to count how many characters have odd counts
    for ch in lowercase:  # to count character occurrence
        if ch in hash_map:  # already in hash map
            hash_map[ch] += 1  # increment count
            if hash_map[ch] % 2 == 1:  # if count is odd, increase counter, else decrease
                odd_counter += 1
            else:
                odd_counter -= 1
        else:  # not in hash_map
            hash_map[ch] = 1
            odd_counter += 1  # 1 is always odd, so increase odd_counter
    if (is_odd and odd_counter != 1) or ((not is_odd) and odd_counter != 0): return False  # palindrome check
    return True  # must be a palindrome
