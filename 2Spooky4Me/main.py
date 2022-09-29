file = open("input.txt", "r").readlines()
lines_length = int(file.split(" ")[0].split(" ")[0])
house_count = int(file.split(" ")[0].split(" ")[1])
high_spooky_score = int(file.split(" ")[0].split(" ")[2])
total_spooky = 0
min_house = 0
max_house = 0
file[lines_length+1].split(" ")[0] = min_house
file[1].split(" ")[1] = max_house
for i in range(lines_length):
    total_spooky += file[i+1].split(" ")[2]
total_house = int(max_house) - int(min_house)
print(100 - int(total_house))