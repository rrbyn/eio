import sys

f = sys.stdin

dict1 = {}
dict2 = {}
dict3 = {}
n = int(f.readline())

for i in range(n):
    name = f.readline()
    namesLists = name.split()
    dict1[namesLists[0]] = namesLists[1]

for i in range(n):
    name2 = f.readline()
    names2Lists = name2.split()
    dict2[names2Lists[0]] = names2Lists[1]


for x in dict1:
    for y in dict2:
        if x == y:
            dict3[dict1[x]] = dict2[y]

for x in dict3:
    sys.stdout.write(x + " " + dict3[x] + "\n")
        







