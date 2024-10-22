    n = int(input())
    nums = input().split()

    nums = [abs(int(_)) for _ in nums]

    manhattan = 0
    euclidian = 0
    chebyshev = max(nums)

    for i in range(n):
        manhattan += nums[i]
        euclidian += nums[i]**2
        
    euclidian = euclidian**(1/2)
        
    print(manhattan)
    print(euclidian)
    print(chebyshev)