class DSU:
    def __init__(self):
        ...

    def nodes_connected(self, n):
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)

        def connected(x, y):
            return find(x) == find(y)

        union(0, 1)
        union(1, 3)
        union(3, 4)

        print(connected(0, 2))
        print(connected(0, 3))
        print(connected(3, 4))


dsu_algo = DSU()
dsu_algo.nodes_connected(9)


