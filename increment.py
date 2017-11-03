def increment(n):
    '''
    objective: to increment value of passed numeric argument by 1
    return Value: increamented value
    '''
    n=n+1
    return n
def add(num1,num2):
    '''
    Objective : To add two numbers
    Input : two numbers
    Approach: Recursive
    return Value: sum of two numbers
    '''
    if num2<0:
        return add(num1-1,increment(num2))
    elif num2==0:
        return num1
    else:
        return add(increment(num1),num2-1)
def pred(num,i=-25):
    '''
    Objective : To find predecessor of a number 
    approach: Recursive
    Return Value: number one less to the passed argument
    
    '''
    if num==1:
        return 0
    else:
        x=increment(i)
        if x==num:
            return i
        else:
         return pred(num,increment(i))
def multiply(num1,num2):
    '''
    Objective: to multiply two numbers
    Approach: Recursive using addition function
    Return value: product of two numbers num1 and num2
    
    '''
    if num2==0:
        return 0
    else :
        return num1+multiply(num1,num2-1)
def subtract(num1,num2):
    '''
    objective : subtract num2 from num1
    Return Value:non differnce of num1 and num2
    approach: recursive
    
    '''
    if num2<0:
        return subtract(increment(num1),increment(num2))
    elif num2==0:
        return num1
    else:
        return subtract(pred(num1),pred(num2))
def divide(num1,num2,i=0):
    '''
    objective: divide num1 by num2
    approach: recursive and using subtract method
    
    '''
    if num1<num2:
        return i
    else:
        i=i+1
        return divide(subtract(num1,num2),num2,i)
    
    

