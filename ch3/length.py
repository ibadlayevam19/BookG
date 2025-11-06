def length(x):
    if (x[0]==x[-1]):
        return 1
    else:
        return 1+length(x[1:])
print(length([1,2,3,4]))