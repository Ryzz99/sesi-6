#A B A B A
#B A B A B
#A B A B A
#B A B A B

row = 4
col = 5
karakter = ['A', 'B']

for i in range(row):
    for j in range(col):
        print(karakter[(i + j) % 2], end=" ")
    print()
