p1= input()
p2= input()
for i in p1:
    if i in p2:
        p1= p1.replace(i,"")
print(p1)
