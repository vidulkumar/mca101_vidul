def findleast(lst,lb,ub,least = 0,lc=0,flag=0):
    if(flag==0):
        least=lst[lb]
        lc=lb
        flag=1
    
    if(lb==ub+1):
        return lc
    elif(least<lst[lb]):
        return findleast(lst,lb+1,ub,least,lc,flag)
    else:
        least=lst[lb]
        lc=lb
        return findleast(lst,lb+1,ub,least,lc,flag)


def selsort(lst,count=0):
    if(lst==[]):
        return
    elif(count==len(lst)-2):
        return
    else:
       leastindx=findleast(lst,count+1,len(lst)-1)
       
       ele = lst[leastindx]   
       del lst[leastindx]
       lst.insert(count,ele)
       selsort(lst,count+1)
a=[3,2,4,0,1]
selsort(a)
       
