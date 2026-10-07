def bubblesort(ar):
    n=len(ar)
    for i in range(n-1):
        for j in range(n-i-1):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1]=ar[j+1],ar[j]
    print(ar)


a=[2,4,7,1,9,6]
print(bubblesort(a))
