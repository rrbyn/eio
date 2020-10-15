f = open("nimsis0.txt", "r")

n = int(f.readline())
people = {}

for i in range(n):
    name = f.readline()
    nameList = name.split()
    firstName = nameList[0]
    if firstName not in people:
        firstName = {
            "tal" : "0",
            "har" : "0"
        }
        people.update(firstName)
print(people)

    