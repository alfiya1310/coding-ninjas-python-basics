def reverseArray(array, start, end, length):
    
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

length = int(input())
array = [int(i) for i in input().split()]

reverseArray(array, 0, length - 1, length)
print(*array)