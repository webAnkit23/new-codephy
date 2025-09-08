import random
text = input("enter the text to be encryted   ")
encrypted = ""
decrypted = ""
for ch in text :
   if(ch.isalpha()) :
         base = ord("a") if ch.islower() else ord("A")
         encrypted += chr((ord(ch) - base + 4) % 26 + base)
   else :
       encrypted +=ch 
        

for ch in encrypted :
   if(ch.isalpha()) :
         base = ord("a") if ch.islower() else ord("A")
         decrypted += chr((ord(ch) - base - 4) % 26 + base)
   else :
       decrypted +=ch 
        
       
print(encrypted)
print(decrypted)



