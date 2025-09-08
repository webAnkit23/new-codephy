base = int(input("enter the base of the number"))
number = input("Enter the number in the given base")



whole , frac = number.split(".")
inc = 0
decimal = 0

for ch in whole[::-1] :
    decimal +=  int(ch) * (base**inc)
    inc+=1

for ch in frac :
     decimal += int(ch) * (base ** (-inc))

print(decimal)
