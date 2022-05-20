# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at
# the end to hold the additional characters, and that you are given the "true" length of the string.

"""
This code will take O(n) time and space. We use python's built in str.join() method to avoid the costly "+"
string concatenation.
"""


def urlify(s: str, n: int):
    if len(s) == n: return s # if the length of the string and the true length are equal, then no changes
    updated = []
    for char in s: # iterate through every character
        if char == " ":
            updated.append("%20") # if the character is a space we append a "%20"
        else:
            updated.append(char) # else, we append the character itself.
    return "".join(updated)



