N = int(input())
sum = 0
for number in range(1, N + 1):
    if (number % 2 == 0):
        sum = sum + number
print(sum)