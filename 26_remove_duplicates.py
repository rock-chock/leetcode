"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Given a sorted array nums, remove the duplicates in-place such that each element
appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.
"""
def main():
    #nums = [-1,-1,-1,0,0,1,1,2,2,3,3,4]
    #nums = [1,1,1,1]
    #nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1,1,2]

    print(remove_duplicates_set(nums[:]))
    print(remove_duplicates_while(nums[:]))
    print(remove_duplicates_while_v2(nums[:]))
    print(remove_duplicates_loop_set(nums[:]))
    #print(remove_duplicates_recursion(nums[:], 0))


# 0. Didn't pass tests at leetcode, passed the same tests perfectly on my computer
# Convert array to set and then back to list

# Convert list to set: O(n). Convert set to list: O(n). Return length of list: O(1)
# Total: O(n)
def remove_duplicates_set(nums):
    nums = list(set(nums))
    return len(nums)


#1. Runtime: 632 ms, Memory: 15.5 MB. The fastest.
# Check if item at current index equals to item at previous_index.
# If true, remove item. If false, alter previous_index and index

# Iterate over list: O(n). Delete(pop) from list: O(n-i) #???. Total: O(n)
def remove_duplicates_while(nums):

    length = len(nums)
    if length <= 1:
        return length

    previous_index = 0
    index = 1
    while index < len(nums):
        if nums[index] == nums[previous_index]:
            nums.pop(index)
        else:
            previous_index = index
            index +=1

    return len(nums)


#2. Runtime: 1916 ms, Memory: 15.5 MB
# Check if item at current index equals to item at previous_index.
# If true, remove item. If false, alter previous_index and index

# Helper function remove_count_times uses recursion(O(n)) and remove
# from list method(n), so it's runtime is O(n^2).
# Count items in list is O(n) for each item in a list(iteration is O(n)), it results to approximately n^2.
# O(n^2) and O(n^2) is O(n^2) in total
def remove_duplicates_while_v2(nums):

    length = len(nums)
    if length <= 1:
        return length

    previous_value = nums[0]
    index = 1
    while index < len(nums):
        value = nums[index]
        if value == previous_value:
            remove_count_times(nums, value, nums.count(value)-1)
        else:
            previous_value = value
            index +=1

    return len(nums)

#3. Runtime: 2256 ms, Memory: 15.3 MB
# Remove duplicates using loop that operates on set made of nums

# Helper function remove_count_times uses recursion(O(n)) and remove
# from list method(n), so it's runtime is O(n^2).
# Convertion of list to set is O(n). Iteration is O(n). Count method is O(n)
# for each item in list, so it results to O(n^2). Get length is O(n). Total: O(n^2)
def remove_duplicates_loop_set(nums):
    for item in set(nums):
        value_count = nums.count(item)
        if value_count > 1:
            remove_count_times(nums, item, value_count-1)
    return len(nums)

#4. Runtime: 2388 ms, Memory: 26.4 MB
# broke when leetcode's input was a very long list

# Recursively iterate over list: remove duplicates if count of nums[i] > 1

# Recursion is O(n), but Python's recursion is pretty slow and uses more resources.
# Length is O(1).Count is O(n) for each item on the list, so it results to O(n^2)
"""
# Remove duplicates if count of nums[i] > 1 and move to next index
def remove_duplicates_recursion(nums, i):
    length = len(nums)
    if i > length - 1:
        return length
    else:
        value = nums[i]
        value_count = nums.count(nums[i])
        if value_count > 1:
            remove_count_times(nums, value, value_count-1)
        return remove_duplicates_recursion(nums, i+1)
"""

# Helper fn. Recursively remove duplicates of the given value from the given list
def remove_count_times(nums, value, duplicates_count):
    if duplicates_count == 0:
        return
    else:
        nums.remove(value)
        return remove_count_times(nums, value, duplicates_count-1)


if __name__ == '__main__':
    main()
