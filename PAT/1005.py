raw = input()
tot = 0
for c in raw:
    tot += int(c)

name = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
output = []
for digit in str(tot):
    output.append(name[int(digit)])

print(" ".join(output))
    
