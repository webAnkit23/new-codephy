color = input("input the color of the cylinder")
contents =  ""
if color == "O" or color == "o" :
      contents = "A     mmonia"
elif color == "Y" or color =="y" :
      contents = "Hydrogen"
elif color == "B" or color =="b" :
      contents = "Carbon monoxide"
elif color == "G" or color =="g" :
      contents = "Oxygen"
else :
      contents = "Contents Unknown"


print(contents)
