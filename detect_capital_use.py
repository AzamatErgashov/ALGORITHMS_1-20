def detectCapitalUse(word):
    if word.isupper() or word.islower():
        return True
    
    return word[:1].isupper() and word[1:].islower()

# biz funksiyalarni qulda yozsak buladi ACKI table dan foydalanib



def isupper(s):
    start, end = 65, 90
    for char in s:
        if not start <= ord(char) <= end:
            return False
    return True

def islower(s):
    start, end = 97, 122
    for char in s:
        if not start <= ord(char) <= end:
            return False
    return True

def detectCapitalUse(s):
    if s.isupper() or s.islower():
        return True
    
    return s[:1].isupper() and s[1:].islower()