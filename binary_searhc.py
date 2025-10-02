mylist = [1,2,3,4,5,6,7,8,9,10]
low = 0
high = len(mylist)-1


# print(mylist[mid-1])

outputitem = int(input())
result = 0
for i in range(len(mylist)):
    mid = int((low + len(mylist)-1) / 2)
    guess = mylist[mid]
    if guess == outputitem:
        print(mid)
    if guess > outputitem:
        high = mid - 1
    elif guess < outputitem:
        low = mid + 1

# print(mid)