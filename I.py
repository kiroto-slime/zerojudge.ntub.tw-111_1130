from itertools import combinations
from collections import Counter
letters= list(input())
c= Counter(letters)
sorted_items= sorted(c.items(), key=lambda kv: (kv[1], -ord(kv[0])))
for key, value in sorted_items:
  if value>=1 :   
    print(ord(key), value)
