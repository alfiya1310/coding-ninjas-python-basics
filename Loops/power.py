x, n = map(int,input().split())
power = 1
while n > 0:
    power *= x
    n = n - 1
print(power)