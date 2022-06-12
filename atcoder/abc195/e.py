n = int(input())
s = input()
x = input()

dp = [[] for i in range(n+1)]
dp[n].append(0)

for i in range(n, 0, -1):
    if(x[i-1] == 'A'):
        for r in range(7):
            if(r*10 % 7 in dp[i] and (r*10 + int(s[i-1])) % 7 in dp[i]):
                dp[i-1].append(r)
    if(x[i-1] == 'T'):
        for r in range(7):
            if(r*10 % 7 in dp[i] or (r*10 + int(s[i-1])) % 7 in dp[i]):
                dp[i-1].append(r)

if(0 in dp[0]): print('Takahashi')
else: print('Aoki')
