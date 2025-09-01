n = (int)(input("Enter the no of terms in the sin series"))
x = (int)(input("enter the degree of the sin in radian"))

sum = 1
term = 1
for i in range ( n) :
  
    fact = 1
    for j in range (1, 2*i + 2) :
        fact = fact * j 
    term = (x * (2 * i + 1))/fact

    print(term)
    if n & 1 == 0 :
        sum +=term
    else :
        sum -=term

print(sum)



   

    
    
     
