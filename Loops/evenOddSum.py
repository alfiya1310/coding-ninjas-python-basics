n = int(input())
even = 0
odd = 0

while n > 0:
    last = n % 10
    
    if n %2 == 0:
        even += last
    else:
        odd += last
    
    n = n // 10
print(even,odd)