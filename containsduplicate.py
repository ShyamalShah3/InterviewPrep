def containsDuplicate(self, nums: List[int]) -> bool:
    """
    Checks to see if a List of integers contains a duplicate

    We use a hash set to add in the elements of nums
        O(n) to add all the elements into the hash set
        O(1) to check if an element already exits in the hash set

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
