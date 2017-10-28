def hanoi(n,source,spare,target):
    if n==1:
        print('move disk from ',source,' to',target)
    else:
        hanoi(n-1,source,target,spare)
        print('move disk from ',source,' to',target)
        hanoi(n-1,spare,source,target)
