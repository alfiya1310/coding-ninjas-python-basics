n = int(input())

if n < 0:
    print("Error")
elif n == 0:
    print(1)
else:
    i = n
    fact = 1
    
    while(n // i != n):
        fact = fact * i
        i = i - 1
        
    print(fact)