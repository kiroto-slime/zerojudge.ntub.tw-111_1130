n= int(input().strip())
total= 1<<n
for i in range(total):
    gray= i^(i>>1)
    s= format(gray, 'b').zfill(n)
    print(s)
