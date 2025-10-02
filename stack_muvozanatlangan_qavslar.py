def is_balanced(s):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
            print(stack, '-')
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                print(pairs[ch])
                return False
                
            stack.pop()
    return not stack

print(is_balanced("({[]})()"))  # True
print(is_balanced("({[)}"))   # False



# s = '(){'

# stack = []
# pairs = {')':'(', ']':'[', '}':'{'}

# for ch in s:
#     if ch in '({[':
#         stack.append(ch)
#     elif ch in ')}]':
#         if not stack or stack[-1] != pairs[ch]:
#             print("xato")
#             break
#         stack.pop()
# else:  # faqat for tsikli xatosiz tugasa ishlaydi
#     if not stack:
#         print("tugri")
#     else:
#         print("xato")