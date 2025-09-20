z= input().strip()
nums= list(map(int, input().split()))
n= int(z)
if n== 0:
    print(0)
else:
    dp= [1]*n
    for i in range(n):
        for j in range(i):
            if nums[j]<nums[i]:
                dp[i]= max(dp[i], dp[j]+1)
    print(max(dp))
