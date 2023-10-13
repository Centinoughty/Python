def flames(name1, name2):
    flames = ["F", "L", "A", "M", "E", "S"]
    name1 = list(name1)
    name2 = list(name2)
    for i in name1:
        if i in name2:
            name2.remove(i)
            name1.remove(i)
            new_name = name1 + name2
        else:
            pass

    while len(flames) > 1:
        index = int(abs(len(new_name) % len(flames))-1)
        flames.remove(flames[index])

    return flames
