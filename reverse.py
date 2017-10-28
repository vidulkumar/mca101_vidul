def reverse(lst,count=0):
    if count==(len(lst))//2:
        return
    else:
        temp=lst[count]
        lst[count]=lst[-(count+1)]
        lst[-(count+1)]=temp
        reverse(lst,count+1)

a=[1,2,3,4,5,10,8]
reverse(a)
print(a)
