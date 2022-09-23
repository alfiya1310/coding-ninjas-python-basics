from sys import stdin

def removeConsecutiveDuplicates(string) :
    n = len(string)

    if n == 0 :
        return string

    answer = string[0]
    i = 1
    
    while i < len(string):
        
        if string[i] != string[i - 1]:
            answer += string[i]
            
        i += 1
        
    return answer
            
#main
string = stdin.readline().strip()
ans = removeConsecutiveDuplicates(string)
print(ans)