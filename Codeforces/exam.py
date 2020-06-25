d,total_hours= [int(_) for _ in input().split()]
min=[]
max=[]
minsum=0
maxsum=0
for i in range(d):
    min1,max1=[int(_) for _ in input().split()]
    minsum+=min1
    maxsum+=max1
    min.append(min)
    max.append(max1)


if(minsum>total_hours or maxsum<total_hours):
    print("NO")
else:
    print("Yes")
    total_hours=total_hours-max[0]
    if total_hours>=0:
        print(str(max[0])+" "+str(total_hours))
        



