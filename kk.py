def left_triangle(n):
    for i in range(n):
        for j in range(n):
        print("*" if j <= i else " ", end="")
        print()