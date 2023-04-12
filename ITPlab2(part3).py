for i in range(1,7):
    print("#", end="")
    for j in range(i):
        if j == i - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()