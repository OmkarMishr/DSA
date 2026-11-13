def TwoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

n = list(map(int,input("Enter a list of no. :").split()))
t = int(input("Enter the target: "))
print(TwoSum(n,t))
