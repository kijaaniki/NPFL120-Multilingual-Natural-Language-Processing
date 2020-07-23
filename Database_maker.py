import requests
r = requests.get("https://wals.info/languoid/genealogy")
G = []
f = str(r.text).split('class="Genus"')
F = open("Genus.csv","a")

for genus in f:    
    part = ((genus.split('/label>')[0]).split('">')[1]).split('<')[0]
    langs = ((genus.split('/label>')[1]).split('</ul')[0]).split('class="Language"')
    for line in langs:
        if 'href' in line:
            wals = (line.split('wals_code_')[1]).split('"')[0]
            lang = (line.split('">')[1]).split('</a')[0]
            t = str(part)+','+str(lang)+','+str(wals)+'\n'
            print(t)
            F.write(t)


