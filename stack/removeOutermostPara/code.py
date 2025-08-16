
def remOuterPara(s: str) -> str:
    res = []
    counter = 0
    for i in range(len(s)):
        if s[i] == '(':
            counter += 1
            if counter > 1:
                res.append(s[counter])
        else:
            counter -= 1
            if counter > 0:
                res.append(s[counter])

    return ''.join(res)

def valiPara(s: str) -> str:
    counter = 0

    #edge case
    if counter < 0: 
        return "invalid para"

    for i in range(len(s)):
        if s[i] == "(":
            counter += 1
        else:
            counter -= 1
    if counter == 0:
        return "valid para"
    # 


def valiParaRec(s: str, c: int, ind: int) -> bool:
    if c < 0:
        return False
    if ind == c:
        return c == 0

    if s[ind] == "(":
        return valiPara(s[ind], c+1, ind+1)
    if s[ind] == ")":
        return valiPara(s[ind], c-1, ind+1)
    if s[ind] != '(':
        return validPara(s[ind], c-1, ind+1)



def remOuterPara_two(s: str) -> str:
    res = []
    count = 0
    n = len(s)
    for i in range(n): 
        if s[i] == "(":
            count += 1
            if count >= 2:
                res.append(s[i])
        else:
            count -= 1
            if count >= 1:
                res.append(s[i])
            

    return ''.join(res)


print(remOuterPara_two("(()())(())"))
print(remOuterPara('(()()()))'))
print(valiParaRec('(()()))', 0, 0))

            


            

