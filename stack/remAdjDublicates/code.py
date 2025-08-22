def remAdjDubli(s: str) -> str:
    res = []
    for i in range(1, len(s)):
        if s[i] not in res:
            res.append(s[i])
        if s[i-1] == s[i]:
            res.pop()
    return ''.join(res)


def countDublicates(s: str) -> str:
    ...

print(remAdjDubli("axxzzy"))
