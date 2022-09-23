def removeAllOccurrencesOfChar(string,c):
    
    output = ""  
    for i in string:
        if i != c:
            output += i
                        
    return output

string = input()
c = input()
output = removeAllOccurrencesOfChar(string,c)
print(output)
