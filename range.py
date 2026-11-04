limit = int(input("Enter the limit: "))

for row in range(1, limit):
    for colm in range(limit - row):
        print(" ", end="")

    for colm in range(1, row + 1):
        print("*", end=" ")

    print()

