str1 = input("enter the first string")
str2 = input("enter the second string")
i = 0
if len(str1) != 0 and len(str2) != 0:
    while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
        i += 1
    print(str1[:i])
if i == 0 :
    print("no common prefix")
        
        
     