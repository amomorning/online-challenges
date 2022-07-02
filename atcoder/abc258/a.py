t = int(input())

h = t // 60
m = t % 60

print("%02d:%02d" % (h+21, m))
