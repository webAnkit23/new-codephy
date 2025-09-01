#Pascal's Triangle
"""
1
11
121
1331
14641  """

n = 5
for i in range(n):
    num = 1
    for j in range(i+1):
        print(num, end="")
        num = num * (i - j) // (j + 1)
    print()
