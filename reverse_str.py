s = ["h","e","l","l","o"]
# print(s[::-1])

# second edition

# i, j = 0, len(s) - 1

# while i < j:
#     s[i], s[j] = s[j], s[i]
#     i += 1
#     j -= 1

# print(s)

s = ['s','l']
def reverse(s):
  rigt = 0
  left = len(s) - 1
  for _ in range(len(s) - 1 ):
    s[rigt], s[left] = s[left], s[rigt]
    rigt += 1
    left -= 1
  
  return s

def reverseString(s):
	return reverse(s)

print(reverseString(s))


