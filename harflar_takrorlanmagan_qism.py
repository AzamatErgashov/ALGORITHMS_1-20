# s = "pwwkew"

# def lengthOfLongestSubstring(s: str) -> int:
#     answer = 0
#     n = []
#     for i in s:
#         if i in n:
#             n.remove(i)
#         elif i not in n:
#             n.append(i)
#     return n

# print(lengthOfLongestSubstring(s))

# second but first is not working

# s = "pwwkew"

# def lengthOfLongestSubstring(s: str) -> int:
#     charSet = set()
#     l = 0
#     res = 0

#     for r in range(len(s)):
#         while s[r] in charSet:
#             charSet.remove(s[l])
#             l+=1
#         charSet.add(s[r])
#         res = max(res, r - l + 1)
#     return charSet


# print(lengthOfLongestSubstring(s))

# third one

s = "pwwkew"

def lengthOfLongestSubstring(s: str) -> int:
    mylist = []
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in mylist:
            mylist.remove(s[l])
            l+=1
        mylist.append(s[r])
        res = max(res, r - l + 1)
    return res


print(lengthOfLongestSubstring(s))