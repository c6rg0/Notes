
def merge (list1,list2): # Subroutines which gets called in 
                         #the main program
    mergeList = [] # Making an array
    i, j = 0, 0
    while (i < len(list1)) and (j < len(list2)):
        if list1[i] < list2[j]:
            mergeList.append(list1[i])
            i += 1
        else:
            mergeList.append(list2[j])
            j += 1
    
    while i < len(list1):
        mergeList.append (list1[i])
        i += 1
    
    while j < len(list2):
        mergeList.append (list2[j])
        j += 1
    return mergeList
        
list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
#list1 = [2,5,15,36]
#list2 = [18,39]
mergedList = merge(list1,list2)
print("list1: ", list1 )
print ("list2: ", list2)
print("mergedList: ", mergedList)
