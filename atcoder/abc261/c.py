import random


n = int(input())
mp = {}

for i in range(n):
    s = input()
    if s not in mp:
        print(s)
        mp[s] = 0
    else:
        print('%s(%d)'%(s, mp[s]))
    mp[s] += 1

