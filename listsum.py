def listsum(lst):
    '''
    objective : return sum of the list
    approach  : recursively add first number of the list with rest list
                lst[0]+list[1:]
    '''
    if(lst==[]):
        return 0
    else:
        return lst[0]+ listsum(lst[1:])

       
