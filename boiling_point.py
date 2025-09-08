boiling_point = float(input("enter the temperature"))

if boiling_point >= 100 *95/100 and boiling_point <= 100 *105/100 :
          print("Water")
elif boiling_point >= 357 *95/100 and boiling_point <= 357 *105/100 :
          print("Mercury")
elif boiling_point >= 1187 *95/100 and boiling_point <= 1187 *105/100 :
          print("Copper")
elif boiling_point >= 2193 *95/100 and boiling_point <= 2193 *105/100 :
          print("Silver")
elif boiling_point >= 660 *95/100 and boiling_point <= 660 *105/100 :
          print("Gold")
else :
        print("substance unKnown")