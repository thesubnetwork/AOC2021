
counter_inc = 0
first_window = 0
sec_window = 0


with open("Day_1.txt") as f:
    my_list = list(f)

print(my_list[0])
for a in range(len(my_list)-2):

    if a + 3 == len(my_list):
        break

    first_window = int(my_list[a]) + int(my_list[a+1]) + int(my_list[a+2])
    sec_window =  int(my_list[a+1]) + int(my_list[a+2]) + int(my_list[a+3])
    print(first_window, ' ', sec_window, end=' : ')
    
    
    if first_window < sec_window:
        counter_inc += 1
        print(first_window - sec_window,' increase', counter_inc)
    else:
        print(first_window - sec_window, ' decrease', counter_inc)


print(counter_inc)