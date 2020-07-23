import requests
r = requests.get("https://wals.info/languoid/genealogy")
G = []
f = str(r.text).split("\n")

F = open("Genus","a")
for line in f:
    if 'class="Genus"' in line:  
        g = (line.split('title="')[1]).split('">')[0]
        F.write(str(g))
        F.write("\n")
        print(g)
F.close()
