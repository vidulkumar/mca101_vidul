def mysin(x):
    '''
    objective : to compute value of mathematical function sin
    approach  : using infinite series of sin i.e.
                x - x**3/3! + x**5 /5! - . . . ....
                and appling by use of while loop
                termination condition ;
                when absolute term is less than e
     return value; sin : calculated sin value
     '''
                   
    print('execution started')
    term = x
    e = 0.0000000000000001
    n = 1
    sin = 0
    flag = False
    while flag != True:
        pterm = term
        
        sin = sin + term
        term = -((term * (x * x))/((2*n)*(2*n+1)))
        n = n + 1
        diff = term - pterm
        if abs(diff) < e :
            flag = True
        
      
    return sin


