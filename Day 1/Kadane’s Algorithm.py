nums=list(map(int,input().split()))
csum=0
msum=0
for i in range(len(nums)):
    csum+=nums[i]
    if csum<0:
        csum=0
    elif csum>msum:
        msum=csum
print(msum)
