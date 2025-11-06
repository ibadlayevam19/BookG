def biggest(x):
    if(x[0]==x[-1]):
        return x[0]
    else:
        return max(x[0], biggest(x[1:]))
print(biggest([1,4,7,3,4,5]))