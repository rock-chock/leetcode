"""
https://leetcode.com/problems/single-number/
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
def main():
    nums = [1,2,-4,3,1,5,2,3,-4]

    print (find_single_hashtable(nums[:]))


# Iterate over list: if a value is in a hashtable, delete it.
# Otherwise add it to the hashtable. At the end return the only item in hashtable

# Iteration is O(n). Insertion to and deletion from a hashtable is O(1). Total is O(n)
def find_single(nums):

    if len(nums) ==  0:
        return None

    hash = {}
    for i in nums:
        if i in hash:
            del hash[i]
        else:
            hash[i] = 1;

    for key in hash:
        return key



if __name__ == '__main__':
    main()
