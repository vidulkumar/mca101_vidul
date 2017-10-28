def prime(lst,plst=[]):
    if lst==[]:
        return plst
    else:
        x=lst[0]
        plst.append(x)
        m=len(lst)
        for i in lst:
            if(i%x)==0:
                lst.remove(i)
        return prime(lst,plst)
lst=[x for x in range (2,20)]
plist=prime(lst)
print(plist)
