def linearsearch(a,el):
    ar=[]
#multiple occurance
    for i in range(len(a)):
        if a[i]==el:  
            ar.append(i)
    if len(ar)>0:
        return ar
    return -1
#single occurence
    if a[i]==el:
        return 1
    return -1
a=[1,2,3,4,5,6,4]
print(linearsearch(a,4))
a=[1,2,3,4,5,6]
print(linearsearch(a,5))


