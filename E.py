from itertools import combinations
from collections import Counter
z= input()
nums= list(map(int, input().split()))
c= Counter(nums)
for key,value in sorted(c.items()):
    if value>= 1:
        print(key, value)
