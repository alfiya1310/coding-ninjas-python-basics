def printSubstrings(string) :

    #Your code goes here.
    n = len(string)
    
    for i in range(n):
        temp = ""
        
        for j in range(i, n):
            temp += string[j]
            print(temp)
            
#main
string = input()
printSubstrings(string)