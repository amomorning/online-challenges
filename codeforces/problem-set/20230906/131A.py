def check(s):
    for c in s:
        if c.islower():
            return False
    return True

s = input()
if not check(s[1:]):
    print(''.join(s))
else:
    s = list(s)
    for i in range(len(s)):
        if s[i].islower():
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
    print(''.join(s))

