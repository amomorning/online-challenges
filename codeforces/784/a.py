import sys;input=sys.stdin.readline

cas = int(input())

for ca in range(cas):
    score = int(input())

    div = 1
    if score <= 1399:
        div = 4
    elif score <= 1599:
        div = 3
    elif score <= 1899:
        div = 2

    print('Division', div)
