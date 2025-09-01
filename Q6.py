#Print alternating * and numbers.

n = 7
for i in range(1,n):
    for j in range(1,i+1):
        if i%2==0:
            print("*", end="")
        else:
            print(i//2+1, end="")
    print()
