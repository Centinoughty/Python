row = []
list = []
a = int(input("How many rows you want to print? "))
for i in range(0, a):
    string = ""
    new_list = list.copy()
    list.clear()
    list.append(1)
    for j in range(0, len(new_list)-1):
        list.append(new_list[j]+new_list[j+1])
    list.append(1)
    for k in range(0, len(list)):
        string = string + str(list[k]) + " "
        string.strip()
    row.append("string_"+str(i+1))
    row[i] = string

for i in range(0, a):
    difference = int(len(row[a-1]) - len(row[a-i-2]))
    if difference % 2 == 0:
        difference = difference / 2
        row[a-i-2] = " "*int(difference) + str(row[a-i-2])
    else:
        difference = int(difference / 2)
        row[a-i-2] = " "*int(difference) + str(row[a-i-2])

for i in range(0, a):
    print(row[i])
