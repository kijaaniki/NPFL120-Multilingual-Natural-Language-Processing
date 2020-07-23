f = open('disimilarity','r').read().split('\n')
L = []
for line in f:
    print(line)
    L.append(line)
m = max(L,key=L.count)
print(m)

