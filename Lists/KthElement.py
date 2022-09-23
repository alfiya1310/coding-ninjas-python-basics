import sys

def kthLargest(arr,k):
    
    arr.sort()
    z = len(arr) - 1
    mn = sys.maxsize
    count = 0
    
    while z >= 0:
        
        if(arr[z] < mn):
            mn = arr[z]
            count += 1
            
        if count == k:
            return arr[z]
        
        z -= 1
        
    return -1
              
def kthSmallest(arr,k):  
    arr.sort()
    count = 0
    mn = -1
    
    for i in range(len(arr)):       
        if arr[i] > mn:
            mn = arr[i]
            count += 1
            
        if count == k:
            return arr[i]
        
    return -1

def kthSmallestLargest(arr,k):
    
    large = kthLargest(arr,k)
    small = kthSmallest(arr,k)   
    return small,large
    
t = int(input())

while t > 0:
    
    n,k = map(int,input().split())
    arr = [int(i) for i in input().split()]
    small,large = kthSmallestLargest(arr,k)
    print(large,small)
    
    t -= 1
