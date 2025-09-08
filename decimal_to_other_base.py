decimal = input("Enter the decimal number")
base = int(input("enter the base u want to convert < 10"))
parts = decimal.split(".")

whole = int(parts[0])
ans =""
while whole > 0 :
    ans = str(whole % base) + ans
    whole = whole//base
ans = ans +"."
if len(parts) == 2 :
        frac = int(parts[1])
        max_count =0
        while max_count < 8 and frac !=0 :
              max_count += 1
              new_frac = frac * base
              if len(str(new_frac)) > len(str(frac)) :
                      ans += str(new_frac)[0]
                      frac = int(str(new_frac)[1:])
              else :
                     ans +="0"
                     frac = new_frac
                

print(ans)
    
            
                     
           
                

         