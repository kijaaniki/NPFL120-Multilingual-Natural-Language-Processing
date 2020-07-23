#Task 1: WALS code = 0
#Task 2: Genus = 6

import numpy as np
from collections import Counter

def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

def getList(dict): 
    return dict.keys() 

Lang_Data = []

data = open("language.tsv").read().split('\n')

for i in range(1,len(data)):
    el = data[i].split("\t")
    El = []
    if not len(el)==1:
        Lang_Data.append(el)

l_data = np.asarray(Lang_Data)[:,4:] #The feature matrix
wals = (np.asarray(Lang_Data)[:,0]).tolist() #WALS code list
#print(l_data.shape) #(2679, 198)

Meta = []

for col in range(l_data.shape[1]): #looping thorugh the columns
    u = (np.unique(l_data[:,col])).tolist() #extract the unique elements from each column
    D = {} 
    for item in range(len(u)): #Browse through the list of the unique elements of each column
        i = u[item]
        if i == '':
            D[i]='NaN'
        else:
            D[i] = item   
    Meta.append(D) #The NaN appended feature matrix
    

Data_Mod = []

for row in range(l_data.shape[0]): #loop through the rows of the feature matrix
    line = l_data[row] 
    C = []
    for col in range(len(line)): #loop through the column values of the extracted line
        c = l_data[row,col] #feature value
        m = Meta[col] 
        C.append(m[c])
    Data_Mod.append(C)

Data_M = np.asarray(Data_Mod)
       
t = input("Enter WALS code: ")
ind = ' '

for name in wals:
    if name==t:
        ind = wals.index(name)


Langs = {}
for lang in range(len(l_data)):
    if lang!=ind:
        j= jaccard(Data_M[ind].tolist(),Data_M[lang].tolist())
        Langs[wals[lang]] = j

c = Counter(Langs)
mc = c.most_common(5)
print(mc)

