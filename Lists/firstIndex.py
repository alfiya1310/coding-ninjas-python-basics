def firstIndex(array, n, target):
    index = -1
    
    for i in range(n):
        if array[i] == target:
            return i
        
    return -1

length = int(input())
array = [int(i) for i in input().split()]
target = int(input())

print(firstIndex(array, length, target))