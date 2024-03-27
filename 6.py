row = 5
col = 5

for i in range(row, 0, -1):
    for j in range(1, col + 1):
        if j < i:
            print("+", end=" ")
        else:
            print(j, end=" ")
    print()
