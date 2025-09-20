def count_bits(n):
    res= 0
    i= 0
    while (1<<i)<= n:
        cycle= 1<<(i+1)
        full= n//cycle
        res+= full*(cycle>>1)
        rem= n%cycle
        res+= max(0, rem-(cycle>>1)+1)
        i+= 1
    return res

n= int(input())
print(count_bits(n))
