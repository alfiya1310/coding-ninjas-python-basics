def lastIndex(array, n, target):
    index = -1
    
    for i in range(n - 1, -1, -1):
        if array[i] == target:
            index = i
            break
        
    return index

length = int(input())
array = [int(i) for i in input().split()]
target = int(input())

print(lastIndex(array, length, target))