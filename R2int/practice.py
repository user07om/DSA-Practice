from collections import defaultdict
def rtwoi(s: str) -> int:
    numarals = defaultdict(int)
    numarals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    count = 0
    for i in range(len(s)-1, 0, -1):
        if numarals[s[i]] > numarals[s[i-1]]:
            result += numarals[s[i]]
            print(result, "-----inner", s[i])
        else: 
            result -= numarals[s[i-1]]
            print(result, "-----outer", s[i])
    return result

print(rtwoi("XLII"))


