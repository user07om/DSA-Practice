class levelOne:
    def __init__(self):
        ...

    def cont_dubli(self, arr):
        seen = set()
        for x in arr:
            if x in seen:
                return True
            seen.add(x)

        return False

    def count_distince(self, arr):
        return len(set(arr))
