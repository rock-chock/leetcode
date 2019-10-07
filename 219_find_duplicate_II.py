"""
https://leetcode.com/problems/contains-duplicate-ii/
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and
the absolute difference between i and j is at most k.
"""

def main():
    nums = [1,2,3,1,2,3]
    k = 2

    # solution to duplicates 2
    print('find_duplicates_2: ', find_duplicates_2(nums[:], k))


# https://leetcode.com/problems/contains-duplicate-ii/
# True if nums[i] == num[j] and j-i <= k
# !!!! doesn't work with big list! runtime error Create new solution
def find_duplicates_2(nums, k):
    s = set(nums)

    if len(nums) == len(s):
        return False


    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]==nums[j] and (j-i) <= k:
                return True
    return False



if __name__ == "__main__":
    main()
