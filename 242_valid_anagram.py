"""
https://leetcode.com/problems/valid-anagram/
Given two strings s and t , write a function to determine if t is an anagram of s.
"""
def main():
    #s = "anagram"
    #t = "nagaram"
    s ="cata"
    t ="ccat"

    print(is_anagram_sort(s, t))
    print(is_anagram_hash(s, t))


# Convert each string to list and sort them. Then convert them back to strings
# and compare.

# Convert to list is O(n). Sort in (n log n). Join is O(n). Total is O(n log n)
def is_anagram_sort(s, t):
    if len(s) != len(t):
        return False

    s_char = list(s)
    t_char = list(t)
    s_char.sort()
    t_char.sort()
    return ''.join(s_char) == ''.join(t_char)


# Add items from s to hashtable s_hash. Iterate over s_hash, check if each item
# is in t and if it's count in t equals to s_hash[i]. If not, immediately return false

# Get length of list - O(1). Convert a list to set is O(n). Iterating over set
# is O(n), but set's length is shorter than of list's of duplicates.
# Count occurence of item in list is O(n), and it is inside loop, total is O(n^2)
def is_anagram_hash(s, t):
    if len(s) != len(t):
        return False

    s_hash = {}
    for i in set(s):
        s_hash[i] = s.count(i)

    for key in s_hash:
        if key not in t or s_hash[key] != t.count(i):
            return False
    return True




if __name__ == '__main__':
    main()
