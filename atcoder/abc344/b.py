
def read():
    s = input()
    if int(s) != 0:
        read()
    print(s)

read()