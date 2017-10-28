def gcd(m,n):
        '''
        objective: to compute the gcd of two numbers m and n
        input values : two numbers m and n
        approach : apply euclid's theorem i.e. recursively find gcd of remainder and quetient
    
        return value : calculated gcd 
        '''
        if ( m < n ):
            temp=m
            m=n
            n=temp
        if( m%n == 0 ):
            return n
        else :
            r = m%n
            return(gcd(n,r))
     
