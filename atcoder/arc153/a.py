tot = 0
alldigits = []
for i in range(1, 10):
    for a in range(0, 10):
        for b in range(0, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    for c in range(0, 10):
                        alldigits.append(f"{i}{i}{a}{b}{j}{j}{k}{c}{k}")


n = int(input())
print(alldigits[n-1])
