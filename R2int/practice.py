from collections import defaultdict
def rtwoi(s: str) -> int:
    numarals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    left = 0
    s_len = len(s)-1
    result = 0
    while left <= s_len:
        if numarals[s[left]] < numarals[s[left+1]]:
            result += numarals[s[left]]
            print(result, "if")
        else:
            result -= numarals[s[left]]
            print(result, "else")

        left += 1
        return result  
print(rtwoi("XLII"))


