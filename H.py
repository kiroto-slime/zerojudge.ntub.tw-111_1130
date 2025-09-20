x= list(map(str, input().split()))
while int(x[0])!= 0:
    num= len(x[1])//int(x[0])
    groups= [x[1][i:i+num] for i in range(0, len(x[1]), num)]
    rev_group= []
    for s in groups:
        rs= ''.join(reversed(s))
        rev_group.append(rs)
    print(''.join(rev_group))
    x= list(map(str, input().split()))
