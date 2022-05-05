t = int(input())

while(t > 0): 
    t -= 1

    s = input()

    first0 = s.find('0')
    last1 = len(s) - s[::-1].find('1') - 1

    if(first0 == -1):
        first0 = len(s)-1
    if(last1 == len(s)):
        last1 = 0
    print(first0 - last1+1)
