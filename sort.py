  
def insertp(lst, element,count=0):
  '''
  Objective : 
  Input Variables :
  Output : 
  '''
    
    if element<lst[0]:
        lst.insert(0,element)
        return
    
    
    elif element>lst[count] and element<lst[count+1]:
        lst.insert(count+1,element)
        count=count+1
        return
    else:
        count=count+1
        insertp(lst,element,count)
           

def sortlist(lst,count=0):
  '''
  Objective : 
  Input Variables :
  Output : 
  '''
    if count==len(lst)-1:
        return
    elif lst[count]<lst[count+1]:
        count=count+1
        return sortlist(lst,count)
    else:
         temp=lst[count+1]
         del lst[count+1]
         insertp(lst,temp)
         count=count+1
         return sortlist(lst,count)
    
a=[3,5,2,1,7,4]
sortlist(a)
        
