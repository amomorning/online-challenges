n = int(input())

def parse_time(s): 
    hh, mm, ss = s.split(':')
    return (int(hh), int(mm), int(ss))

mn = (23, 59, 59)
mx = (00, 00, 00)
mni, mxi = '', ''
for i in range(n):
    id_number, sign_in, sign_out = input().split()
    if(parse_time(sign_in) < mn):
        mn = parse_time(sign_in)
        mni = id_number
    if(parse_time(sign_out) > mx):
        mx = parse_time(sign_out)
        mxi = id_number

print("{} {}".format(mni, mxi))
    
    
    
