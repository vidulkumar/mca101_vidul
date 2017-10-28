def mycos(x):
    '''
    objective : to compute value of mathematical function sin
    approach  : using infinite series of sin i.e.
                1 - x**2/2! + x**4 /4! - . . . ....
                and appling by use of while loop
                termination condition ;
                when absolute term is less than e
     return value; sin : calculated sin value
     '''
                   
    print('execution started')
    term = -(x*x)/2
    e = 0.0000000000000001
    n = 1
    cos = 1
    flag = False
    while flag != True:
        pterm = term
        n = n + 1
        cos = cos + term
        term = -((term * (x * x))/((2*n-1)*(2*n)))
        
        diff = term - pterm
        if abs(term) < e :
            flag = True
        
      
    return cos
