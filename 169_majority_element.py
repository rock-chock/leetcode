"""
https://leetcode.com/problems/majority-element/
Given an array of size n, find the majority element.
The majority element is the element that appears more than [ n/2 ] times.
You may assume that the array is non-empty and the majority element
always exist in the array.
"""

def main():
    nums = [2,2,1,1,1,2,2]

    print(majority_element_hash(nums[:]))

# Constructing set from list is O(n). Iteration over set is O(n), where n is
# number_of_unique_items: if a list mostly consists of duplicates, runtime will be pretty fast,
# best case is O(2) for 2 elements in the list
# Accessing items from set and dictionary is O(1)
# Count is O(n) for each element in set, so it results to O(n^2). Total is O(n^2) #???
# where n can be close to 1 if there are many duplicates in the list,
# the best case can be O(n)
def majority_element_hash(nums):
    hash = {}

    for i in set(nums):
        hash[str(i)] = nums.count(i)

    max_count = 0
    max_key = nums[1]

    for key in hash:
        if hash[key] > max_count:
            max_key = key
            max_count = hash[key]

    if max_count > (len(nums)//2):
        return max_key

    return 0


if __name__ == '__main__':
    main()
