#Allow for GENUS lookup and use  the integration script to find similairty
from Integrate_b import main as integrate
genus = str(input('Enter Genus:\n'))
G = []
F = open('Genus.csv','r').read().split('\n')
for line in F:
    splt = (line.split(','))
    gen = splt[0]
    if gen == genus:
        G.append(line)
if len(G)==0:
    print('Incorrect genus name')
else:
    R = []
    print('\n Languages under genus %s : \n'%genus)
    for lang in G:
        l = lang.split(',')
        t = l[2]
        print(l[1])
        wals = (str(integrate(t)).split(','))[0]
        wals = (wals.replace("'","")).replace('(','')
        R.append(wals)
    m = max(R,key=R.count)
    print('\n\nMost related:')
    for line in F:
        item = line.split(',')
        if m in item:
            print(item[1])

