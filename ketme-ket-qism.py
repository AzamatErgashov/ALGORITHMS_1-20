array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1]


# def isValidSubsequence(array, sequence):
#     # Write your code here.
#     son = 0
#     length = len(sequence)
#     for i in sequence:
#       if i in array:
#         son += 1
#         array = array[array.index(i)+1:]
#         print(array)
#     if son == length:
#       return True
#     else:
#       return False

# print(isValidSubsequence(array, sequence))

# second edition

array_index = 0
sequence_index = 0


while array_index < len(array) and sequence_index < len(sequence):
    if array[array_index] == sequence[sequence_index]:
        sequence_index += 1
    array_index += 1

if sequence_index == len(sequence):
    print('🖕🏿')