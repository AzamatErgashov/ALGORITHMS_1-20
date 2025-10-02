# def rotate(nums: list, k: int) -> list:
#     k = k % len(nums)
#     reverse_list = nums[::-1]
#     reverse_list[:k] = reverse_list[:k][::-1]
#     reverse_list[k:] = reverse_list[k:][::-1]
#     return reverse_list


#. second edition

def reverse(nums, a, b):
    while a < b:
        nums[a], nums[b] = nums[b], nums[a]
        a += 1
        b -= 1

def rotate(mylist, k):
    k = k % len(mylist)
    reverse(mylist, 0, len(mylist) - 1)
    reverse(mylist, 0, k-1)
    reverse(mylist, k, len(mylist) - 1)
    return mylist