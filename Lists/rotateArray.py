def rotateArray(array, n, k):
    
    for i in range(k):
        temp = array[0]
        
        for j in range(n - 1):
            array[j] = array[j + 1]
            
        array[n - 1] = temp

length = int(input())
array = [int(i) for i in input().split()]
k = int(input())

rotateArray(array, length, k)
print(*array)