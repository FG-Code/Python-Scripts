from itertools import permutations
import enchant

d=enchant.Dict("en_UK")

op=set()

inp="download"

lettr = [x.lower() for x in inp]


for n in range(5, len(inp)):
    for y in list(permutations(lettr, n)):
        z="".join(y)
        if len(z)>2:
            if d.check(z):
                op.add(z)


print(op)
