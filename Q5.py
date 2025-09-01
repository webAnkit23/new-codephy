#Diamond Pattern

n = 6
m = 4
for i in range(1,n):
    for j in range(n-i-1,0, -1):
        print(" ", end="")
    for j in range(1, i+1):
        print("* ", end="")
    print()
for i in range(m, 0, -1):
    for j in range(0,m-i+1):
        print(" ", end="")
    for j in range(1,i+1):
        print("* ", end="")
    print()

