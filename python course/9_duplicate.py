list= ["a", "b", "c", "d", "e", "f", "g", "h", "a", "b", "h"]

dup= []
for value in list:
    if list.count(value) > 1 :
        if value not in dup :
            dup.append(value)

print(dup)

