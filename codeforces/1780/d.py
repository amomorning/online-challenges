
def ask(cur):
    print('-', cur, flush=True)
    return int(input())

def answer(bits):
    ret = 0
    for x in bits:
        ret += 1<<x
    return ret

for _ in range(int(input())):
    cnt = int(input())
    cur = 1
    bits = []
    for i in range(30):
        res = ask(cur)
        if i == 0:
            cur = 1
        else:
            cur += cur

        if res == cnt-1:
            bits.append(i)
        if len(bits) == cnt:
            print('!', answer(bits))
            break
        
