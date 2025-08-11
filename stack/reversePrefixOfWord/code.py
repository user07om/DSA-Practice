def revSagement(word: str, ch: str) -> str:
    res = []
    for i in range(len(word)):
        if word[i] == ch:
            res = word[:i+1]
            return res[::-1]+word[i+1:]
    if ch not in word:
        return word
        
        

print(revSagement("abcdefd", "x"))
