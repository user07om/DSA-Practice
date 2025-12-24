
def anagram(s: str, t: str):
    s1 = {}
    s2 = {}
    s = list(s)
    t = list(t)
    for i in range(len(s)):
        if s[i] in s1:
            s1[s[i]] += 1
        else:
            s1[s[i]] = 1

    for i in range(len(t)):
        if t[i] in s2:
            s2[t[i]] += 1
        else:
            s2[t[i]] = 1

    return s1 == s2


#print(anagram("anagram", "nagaram"))
print(anagram("car", "rat"))
