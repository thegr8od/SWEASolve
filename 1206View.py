#1206 View
for i in range(1,11):
    n = int(input())
    height = list(map(int, input().strip().split(" ")))
    cnt = 0
    for j in range(n):
        if j == 0:
            if height[j] > height[j+1] and height[j] > height[j+2]:
                cnt += height[j] - max(height[j+1], height[j+2])
        if j == 1:
            if height[j] > height[j+1] and height[j] > height[j+2] and height[j]>height[j-1]:
                cnt += height[j] - max(height[j+1], height[j+2], height[j-1])
        if j == n-2:
            if height[j] > height[j-2] and height[j] > height[j-1] and height[j]>height[j+1]:
                cnt += height[j] - max(height[j-2], height[j-1], height[j+1])
        if j == n-1:
             if height[j] > height[j-2] and height[j] > height[j-1]:
                cnt += height[j] - max(height[j-2], height[j-1]) 
        else:
            if height[j] > height[j-1] and height[j] > height[j-2] and height[j] > height[j+1] and height[j] > height[j+2]:
                cnt += height[j] - max(height[j-2], height[j-1],height[j+1], height[j+2]) 
    print("#"+str(i),+cnt)                   