S = int(input())
E = int(input())
W = int(input())

for currentFahrenheitValue in range (S, E+1, W):
    celsius = int((currentFahrenheitValue - 32) * 5 / 9)
    print(currentFahrenheitValue, celsius, sep = "\t")