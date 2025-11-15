arr=[2,3,1,2,5]
for pos in range(len(arr)-1):
    min=pos
    for i in range(pos+1,len(arr)):
        if arr[min]<arr[i]:
            i=min
        arr[i],arr[min]=arr[min],arr[i]
print(arr)
