# question 1

def factorial(x):
    if x ==0 or x==1:
        return 1
        
    else:
        return x*factorial(x-1)
        

# question 2

absolute = lambda x,i: x**(2*i) /factorial(2*i) 
def exp_x(x, n):
    
    total =0

    
    for i in range(n):
    
        
        total += (-1)**i * absolute(x,i)
    
            
    return total
        
        
x = int(input())    
n = int(input())
exp_x(x,n)

print(exp_x(x,n))
    
    
# question 3
 
g= 0

def function1(n,r):
    """ This function computes the geometric series using recursion and a global variable. It adds the current term (r to the power of n) to the result and recursion ends when n is 0, adding the final term '1' to the total."""
    
    global g
    
    if n== 0:
        
         g+= 1
         return 
    else:
        g+= r**n
        function1(n-1,r)
    
