
counter_lowers = 0

with open("Day_1.txt") as f:
    my_list = list(f)

print(my_list[0])
for a in range(1,len(my_list)):
    if int(my_list[a]) > int(my_list[a-1]):
        counter_lowers += 1
        print(int(my_list[a]),' increase')
    else:
        print(int(my_list[a]), ' decrease')


print(counter_lowers)