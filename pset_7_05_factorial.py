    # n! = 1*2*3*4*5*6.............n


num = int(input(" Enter the number : ")) 
fac = 1
for i in range(1 , num + 1):
    fac = fac*i
print(f"The factorial of {num} is = {fac}")   


       # if num  is = 5
                 # p = 1*1 = 1 = p
                 # p = 1*2 = 2 = p (new) 
                 # p = 2*3 = 6 = p (new)
                 #   # p = 6*4 = 24 = p(new)
                 #   # p = 24*5 = 120   stop!