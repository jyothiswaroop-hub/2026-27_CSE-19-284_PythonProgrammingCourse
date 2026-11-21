rows = int(input("Enter grid size (rows and columns): "))

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        print("*", end=" ")
    print()