# 1 3 5 6 7
# 2 5 8 11 14
# 3 7 11 15 19
# 4 9 13 17 21
# 5 11 15 19 23

g = 2
for i in range (1,6):
    n = i
    for j in range (5):
        print(n, end=' ')
        n += g
    g += 1
    print( )
