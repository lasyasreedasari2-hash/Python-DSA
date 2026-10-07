def selectionsort(ar):
    n=len(ar)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if ar[j]<ar[min_index]:
                ar[j],ar[min_index]=ar[min_index],ar[j]
    print(ar)

a=[5,2,8,9,1]
print(selectionsort(a))
