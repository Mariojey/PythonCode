file = open("input.txt").readlines()
for i in range(1, file[0]):
    if file[i+1] < file[i]:
        file[i+1], file[i] = file[i], file[i+1]
print(list(file))