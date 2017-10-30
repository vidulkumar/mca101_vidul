def hanoi(n,source,spare,target):
    '''
    Objective : To generate movements needed to solve Tower of Hanoi
    Input Variables : 
        n : No. of disks
        source : The source pole ie. The starting pole where all the disks are originally
        spare : The spare pole which will be used to store disks temporarily
        target : The target pole ie. The destination pole where the disks are meant to go.
    '''
    if n==0:
      return  
    elif n==1:
        print('move disk from ',source,' to',target)
    else:
        hanoi(n-1,source,target,spare)
        print('move disk from ',source,' to',target)
        hanoi(n-1,spare,source,target)
