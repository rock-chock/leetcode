"""
https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
"""

def main():
    s = ['h','e','l','l','o']

    print("list method: ", reverse_list(s[:]))
    print("iterative solution: ", reverse_loop(s[:]) )
    print("recursive: ",  reverse_recursively(s[:]))


# Reverse a list using built-in method reverse()

# Reverse in O(n) https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
def reverse_list(s):
    s.reverse()
    return s


# Iterate over left half of the list, swap values at mirror-symmetrycal indices

# List iteration is O(n).
def reverse_loop(s):
    ind_pair = len(s) - 1
    for i in range(len(s) // 2):
        temp = s[i]
        s[i] = s[ind_pair]
        s[ind_pair] = temp
        ind_pair -=1
    return s


# Recursively iterate over list, return the result when approached to the middle.

# Iteration over list is O(n)
def reverse_recursively(s):
    return rev(s, 0, (len(s)-1))

def rev(s, i, ind_pair):
    if (ind_pair - i) <= 1:
        return s
    else:
        temp = s[i]
        s[i] = s[ind_pair]
        s[ind_pair] = temp
        return rev(s, i+1, ind_pair-1)




if __name__ == "__main__":
    main()
