counter = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            counter +=1
            print(x, y, z)

print("The number of times this looped is "+ str(counter))


for x in ["a", "b"]:
    for y in ["c", "d"]:
        for z in ["e", "f"]:
            counter +=1
            print(x, y, z)
