file = open("input.txt", "r").readlines();
pairs=["db","bd","pq","qp"]
print("Ready")
for i in file:
    if i=='  \n': break
    try: print((pairs.index(i.rstrip())>= 0)*"Mirrored pairs")
    except: print("Ordinary Pair")