"""
https://leetcode.com/problems/move-zeroes/
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
"""

def main():
    #nums = [0,1,0,3,12] #[1,3,12,0,0]
    #nums = [0,0,0,0]
    #nums = []
    #nums = [0,0,1]
    #nums = [1,0,0,3]
    nums = [1,0,0,0,3,0,1]

    print(move_zeroes_while(nums[:]))
    print(move_zeroes_swap(nums[:]))


# Modify nums: when found 0, delete current item and append it to the end of nums
# Iteration is O(n). Pop is O(n-i), append is O(1). Total is O(n^2)
def move_zeroes_while(nums):
    # Check if nums is not empty
    if len(nums) == 0:
        return nums

    # Check if nums contains 0 or consists of only zeroes
    if (0 not in nums) or (len(set(nums)) == 1):
        return nums

    # Iterate over list, find zeroes, remove them and append to nums.
    index = 0
    max_index= len(nums)
    while index < max_index:
        if nums[index] == 0:
            nums.pop(index)
            nums.append(0)
            max_index -= 1
        else:
            index += 1

    return nums

# Modify nums: if found non-zero value, swap it with the item at possible_zero_pos
# Iteration is O(n), accessing the values is O(1). Total is  O(n)
def move_zeroes_swap(nums):
    # Check if nums is not empty
    if len(nums) == 0:
        return nums

    # Check if nums contains 0 or only consists of zeroes
    if (0 not in nums) or (len(set(nums)) == 1):
        return nums

    # If found non-zero, swap items at index and possible_zero_pos and advance the former
    possible_zero_pos = 0
    for index in range(len(nums)):
        if nums[index] != 0:
            nums[possible_zero_pos], nums[index] = nums[index], nums[possible_zero_pos]
            possible_zero_pos += 1

    return nums


if __name__ == "__main__":
    main()
