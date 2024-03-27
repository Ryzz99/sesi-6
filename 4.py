# 1 3 5 7 9
# 2 4 6 8 10
# 3 5 7 9 11
# 4 6 8 10 12
# 5 7 9 11 13

row = 5
col = 5

for i in range (1, row +1):
    b = i
    for j in range (col):
        print (i, end=' ')
        i += 2 
    print()
