# s = ['salom','sal', 'samsung']
# def longest(words):
#     short = min(words, key=len)# key len bu uzunligi buyicha eng kichigini ol degani
#     n = len(short)
#     prefix = ""
#     for i in range(n):
#         for word in words:
#             if short[i] != word[i]:
#                 print(prefix)
#                 return prefix

#         prefix = short[:i+1]
#         print(prefix)
#     return short
# print(longest(s))

# second edition

s = ['salom','sal', 'samsung']
def longest(words):
    short = min(words, key=len)# key len bu uzunligi buyicha eng kichigini ol degani
    n = len(short)
    prefix = 0
    for i in range(n):
        for word in words:
            if short[i] != word[i]:
                print(prefix)
                return word[:prefix]

        prefix = i+1
        print(prefix)
    return short
print(longest(s))