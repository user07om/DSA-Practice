# first approach would be...
def revSagement(word: str, ch: str) -> str:
    res = []
    for i in range(len(word)):
        if word[i] == ch:
            res = word[:i+1]
            return res[::-1]+word[i+1:]
    if ch not in word:
        return word
        

# second approach, might work....
def revSagementSecond(word: str, ch: str) -> str:
    res = []
    i = 0

    while i <= len(word):
        if word[i] == ch:
            res[:i+1]

        i++
        

print(revSagement("abcdefd", "x"))
