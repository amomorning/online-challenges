import sys; input = lambda:sys.stdin.readline().strip("\r\n")

for _ in range(int(input())):
    n = int(input())
    
    cnt = [0] * 26
    for i in range(2*n+1):
        for c in input():
            cnt[ord(c) - ord('a')] += 1
            
    for i, x in enumerate(cnt):
        if x % 2 == 1:
            print(chr(i + ord('a')))
            break


