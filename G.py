import re
times= int(input())
for i in range(times):
    s= input()
    letters= (re.findall(r"[A-Za-z]", s))
    nums= (re.findall(r"\d+", s))
    for e in range(len(letters)):
        print(letters[e]*int(nums[e]), end="")
    print()
