def sort012(arr):

    n = len(arr)
    
    countZero = 0
    countOne = 0
    countTwo = 0

    for i in arr:

        if i == 0:
            countZero += 1

        elif i == 1:
            countOne += 1

        else:
            countTwo += 1

    l = [0] * n
    index = 0

    for i in range(countZero):

        l[index] = 0
        index += 1
        
    for i in range(countOne):
        l[index] = 1
        index += 1

    for i in range(countTwo):
        l[index] = 2
        index += 1
                
    return l

t = int(input())

while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    sorted = sort012(arr)
    print(*sorted)
    
    t -= 1