def f(x):
    a=1
    if x==0:  
        return 1;
    elif x<0 and x!=-1:
        return "-ve numbers don't have factorials";
    for i in range(1,x+1):a=a*i;
    return a;