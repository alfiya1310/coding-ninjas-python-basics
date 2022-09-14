def countBits(n):
    count = 0
    while (n > 0):
        r = n % 2
        if r == 1:
            count += 1
            
        n = n // 2
        
    return count
    
n = int(input())
print(countBits(n))