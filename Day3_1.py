
def split(word):
    return [char for char in word]

gamma = ""
epsilon = ""

with open("Day_3.txt") as f:
    mylist = f.read().splitlines()
    f.close

countList = [0]*len(mylist[0])

for a in mylist:
    for b in range(0,len(a)):
        if bool(int(a[b])):
            countList[b] += 1

print("%s : %s" % (countList,len(mylist)//2))


for a in range(0,len(countList)):
    if countList[a] > len(mylist) // 2:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"

print(int(gamma,2) * int(epsilon,2))
