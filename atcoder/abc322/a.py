n = int(input())

s = input()
if s.find('ABC') != -1:
    print(s.index('ABC')+1)
else:
    print(-1)
