"""
https://leetcode.com/problems/contains-duplicate/
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice
in the array, and it should return false if every element is distinct.
"""

def main():
    #nums = [1,2,3,1,2,3]
    nums = [-1,-1,-1,0,0,1,1,2,2,3,3,4]

    # Use set
    print('set: ', find_duplicates_set(nums[:]))

    # Use loop
    print('loop: ', find_duplicates_loop(nums[:]))


# Create set from given list and compare their lengths
# Convert a list to set: O(n). Get length of a list or a set is O(1). Total: O(n)
def find_duplicates_set(nums):
    s = set(nums)
    return(len(nums) != len(s))


# At each iteration add new value to hashtable.
# Immediately return true if item already was in hash
# Put a value to and get it from hashtable: O(1)
# Iterate over list: O(n). But early return can make it faster
# Best case: O(2)-> O(1). Average case:O(n/2)-> O(n). Worst case: O(n)
# Total: O(n)
def find_duplicates_loop(nums):

    if len(nums) == 0:
        return False

    hash = {}
    for i in nums:
        if i in hash:
            return True
        hash[i] = 1
    return False







if __name__ == "__main__":
    main()
