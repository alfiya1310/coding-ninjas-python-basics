from sys import stdin

def reverseWord(string, start, end) :
    reverse = ""

    while start < end :
        reverse = string[start] + reverse
        start += 1
       
    return reverse

def reverseEachWord(string) :
    
    #Your code goes here.
    n = len(string)
    previousSpaceIndex = -1
    ans = ""
    i = 0
    while i < n :
        if string[i] == ' ' :
            ans += (reverseWord(string, previousSpaceIndex + 1, i) + " ")
            previousSpaceIndex = i

        i += 1

    ans += (reverseWord(string, previousSpaceIndex + 1, i) + " ")

    return ans

#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)