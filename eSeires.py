x = (int)(input("Enter the value of x"))
n = (int)(input("Enter the number of terms"))
sum = 0
for i in range(n) :
    fact = 1
    for j in range (1, i + 1) :
       fact *=j
    i_term = (x ** (i))/fact
    sum +=i_term
    print(i_term)
print(sum)
