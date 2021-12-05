with open("Day_2.txt") as f:
    my_list = f.read().splitlines()
    f.close

depth = 0
pos = 0


for a in my_list:
    print(a)

    if a[0] == "f":
        pos += int(a[-1])
        
    elif a[0] == "u":
        depth -= int(a[-1])
        
    elif a[0] == "d":
        depth += int(a[-1])
        

print(pos * depth)
