'''
Objective: To merge two sorted list
return value: merged list
input parameters: lis1 and list2 two sorted lists
approach: Recursion

'''
import pdb

def merge(list1,list2,list3=[],idx1=0,idx2=0):
    #pdb.set_trace()
    if(len(list3)==len(list1)+len(list2)):
        return list3
    elif len(list1)==idx1:
        list3.extend(list2[idx2:])
        return list3  
    elif len(list2)==idx2 :
        list3.extend(list1[idx1:])
        return list3    
    elif list1[idx1]>=list2[idx2]:
        list3.append(list2[idx2])
        idx2=idx2+1
        return merge(list1,list2,list3,idx1,idx2)
    else:
        list3.append(list1[idx1])
        idx1=idx1+1
        return merge(list1,list2,list3,idx1,idx2)
    
list1=[2,4,70,90]
list2=[1,3,80]
list3=merge(list2,list1)
