x = float(input("enter abssica"))
y = float(input("enter ordinate"))


if x ==0 and y == 0 :
    print("point is at the origin")
elif x > 0 and y > 0 :
    print("point is in the first qudrant")
elif x < 0 and y > 0 :
    print("point is in the second quadrant")
elif x < 0 and y < 0:
    print("point is in the third quadrant")
else :
    print("it is in the furth quadrant")