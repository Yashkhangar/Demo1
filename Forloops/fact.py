"""  Wap to find factorial of a no. """

#5!
""" fact =1 
for i in range(1,6):
    fact *=i # fact = fact*i 
print(fact) """    

""" Universal code """
""" n=int(input("Enter a number"))
fact =1 
for i in range(1,n+1):
    fact *=i # fact = fact*i 
print(str(n)+"! ",fact)    
     """
    
""" wap to print numbre is odd or even from table 1 to 20     """


""" for i in range(1,21):
    if i%2==0:     
        print("i=",i,"The number is even")
    else:
        print("i=",i,"The number is odd")
     """

""" wap to check whethere a number is divisible by 3 and 5 till range 21 """
""" for i in range(1,21):
    if i%3==0 and i%5==0:     
        print(i,"is divisible by 3 and 5")
    else:
        print(i,"is not divisible by 3 and 5")
        """
        
        
        
""" for i in range(1,6):
    n=int(input("Enter a number"))
    if n%3==0 and n%5==0:     
        print(n,"is divisible by 3 and 5")
    else:
        print(n,"is not divisible by 3 and 5")  """       
        
        
""" for i in range(1,11):
    n=int(input("Enter number"))
    if i%2==0:     
        print("n=",n,"The number is even")
    else:
        print("n=",n,"The number is odd") """


for i in range (1,6):
    n=int(input("Enter number"))
    if n%2==0: # or n%3==0 or n%4==0 or n%5==0:
        print("n is divisible by 2")
    if n%3==0:
        print("n is divisible by 3")
    if n%4==0:
        print("n is divisible by 4")    
    if n%5==0:
        print("n is divisible by 5") 
    if n%2!=0 and n%3!=0 and n%4!=0 and n%5!=0:
        print("Not divisible by 2,3,4,5")       
else:
    print("Finished")       
""" name=input("Enter name ")
for i in name:
    if i=="A" or i=="a" or i=="E" or i=="e" or i=="I" or i=="i" or i=="O" or i=="o" or i=="U" or i=="u" :
        print(i,"is a vowel")   
    else:
        print(i,"is not a vowel")  """      
"""    
for i in range(4):  
    a=10
    b= 15 
    operator =input("Enter Operator( +,-,*,/)")
    if operator =="+":
        print("a+b= ",(a+b))   
    elif operator =="-":
        print("a-b= ",(a-b))   
    elif operator =="*":
        print("a*b= ",(a*b)) 
    elif operator =="/":
        print("a/b= ",(a/b))        
    else:
        print("Invalid input")    """
   
   
   
   
   
        