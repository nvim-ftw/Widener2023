def find_min(things):
    min = [-1, 9999999999]
    for thing_num, thing in enumerate(things):
        if thing < min[1]:
            min[0] = thing_num
            min[1] = thing
    return min[0]

all_lens = []
all_mile_lens = []
all_cable_lens = []

distance = int(input())
mile_len = int(input())
cable_len = int(input())

for i in range(25):
    for j in range(25):
        total_len = (mile_len * i) + (cable_len * j)
        x = distance - total_len
        if x < 0:
            x = total_len - distance

        all_lens.append(x)
        all_mile_lens.append(i)
        all_cable_lens.append(j)

x = find_min(all_lens)

print(str(all_mile_lens[x]) + " " + str(all_cable_lens[x]))

for i in range(len(all_lens)):
    if all_lens[x] == all_lens[i]:
        if all_mile_lens[i] == all_mile_lens[x] and all_cable_lens[i] == all_cable_lens[x]:
            continue
        else:
            print(f"{all_mile_lens[i]} {all_cable_lens[i]}")
