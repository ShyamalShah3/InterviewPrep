def containsDuplicate(self, nums: List[int]) -> bool:
    """
    Checks to see if a List of integers contains a duplicate
    
    Constraints:
        1 <= nums.length <= 100000
        -1000000000 <= nums[i] <= 1000000000

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
