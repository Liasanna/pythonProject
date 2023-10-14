n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, " " * (5 - len(str(i * j))), end=" ")
    print("\n", end="")
