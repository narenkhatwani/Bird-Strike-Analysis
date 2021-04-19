sourcefile ="narenbird1.csv"


with open(sourcefile, "r") as germ:
    germ = [item.lower().replace("\n", "") for item in germ.readlines()]
for item in sorted(set(germ)):
    x=item.title(), germ.count(item)
    print(x)

