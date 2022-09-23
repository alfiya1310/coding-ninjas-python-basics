def countWords(string) :
    if len(string) == 0:
        return 0
    
    count = 0
    
    for i in string:
        if i == ' ':
            count += 1
            
    return count + 1