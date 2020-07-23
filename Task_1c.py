#Allow for GENUS lookup and use  the integration script to find similairty
from Integrate_c import main as integrate
F = open('wals','r').read().split('\n')
f= open('disimilarity','a')
for line in F:
    l = line
    #print(l)
    print('Dissimilarity for %s :'%l)
    d = integrate(l)
    mv = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    item = list(mv.keys())[0]
    f.write(item)
    f.write('\n')
    print(item)
f.close()
