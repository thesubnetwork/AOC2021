with open("Day_2.txt") as f:
    my_list = f.read().splitlines()
    f.close

depth = 0
pos = 0
aim = 0
depth_change = 0
unit = 0

for a in my_list:
    print(a)
    unit = int(a[-1])
    if a[0] == "d":
        # depth += unit
        aim += unit
    elif a[0] == "u":
        # depth -= unit
        aim -= unit
    elif a[0] == "f":
        pos += unit
        depth_change = aim * unit
        depth = depth_change + depth
    print("V: %s D: %s A: %s P: %s" % (unit, depth, aim, pos))


print("Final--D: %s A: %s P: %s" % (depth, aim, pos))
print("Answer: %s" %(pos * depth))
