def quicksort(x):
    if len(x)<2:
        return x
    else:
        pivot=x[0]
        less=[i for i in x[1:] if i<=pivot]
        greater=[i for i in x[1:] if i>pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
print(quicksort([4,2,3,7,0,4,1,6]))