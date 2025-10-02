# first solve 

# nums = [-7,-3,2,3,11]
# row = []
# for i in range(len(nums)):
#     row.append(nums[i] * nums[i])
# print(sorted(row))

# second solve

nums = [-4,-1,0,3,10]

i , j = 0, len(nums) - 1
result = []

while i <= j:
    if abs(nums[i]) < abs(nums[j]):
        result.append(nums[j] ** 2)
        j -= 1
    else:
        result.append(nums[i] ** 2)
        i += 1
result.reverse()

print(result)