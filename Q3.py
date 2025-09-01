#Pyramid Pattern

n = 6
for i in range(1,n):
    for j in range(n-i+1,0, -1):
        print(" ", end="")
    for j in range(1, i+1):
        print("* ", end="")
    print()