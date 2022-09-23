file = open("input.txt", 'r').readlines()
lines_length = int(file[0])
for i in range(lines_length):
    num_from_line = list(map(int, file[i+1].split(" ")))
    print(((num_from_line[0]*num_from_line[1]) == num_from_line[2])*+"tak"+((num_from_line[0]*num_from_line[1]) != num_from_line[2])*+"Nie")