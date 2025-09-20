import math

times= int(input().strip())
for i in range(times):
    m, n= map(int, input().split())
    for x in range(m, n+1):
        if x<= 1:
            continue
        is_prime= True
        limit= int(math.sqrt(x))
        for d in range(2, limit+1):
            if x%d== 0:
                is_prime= False
                break
        if is_prime:
            print(x)
