def increment(n):
    n=n+1
    return n
def add(num1,num2):
    if num2<0:
        return add(num1-1,increment(num2))
    elif num2==0:
        return num1
    else:
        return add(increment(num1),num2-1)
def pred(num,i=-25):
    if num==1:
        return 0
    else:
        x=increment(i)
        if x==num:
            return i
        else:
         return pred(num,increment(i))
def multiply(num1,num2):
    if num2==0:
        return 0
    else :
        return num1+multiply(num1,num2-1)
def subtract(num1,num2):
    if num2<0:
        return subtract(increment(num1),increment(num2))
    elif num2==0:
        return num1
    else:
        return subtract(pred(num1),pred(num2))
def divide(num1,num2,i=0):
    if num1<num2:
        return i
    else:
        i=i+1
        return divide(subtract(num1,num2),num2,i)
    
    

