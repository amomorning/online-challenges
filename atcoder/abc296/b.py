
idx= 'abcdefgh'
for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == '*':
            ans = idx[j]+str(8-i)
print(ans)
            
