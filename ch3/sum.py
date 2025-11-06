def summ(x):
    if(x[0]==x[-1]):
        return x[0]
    else:
        return x[0]+summ(x[1:])
print(summ([1,2,3]))