arr=[1,2,4,5,2]
x=3
for i in range(len(arr)):
    if arr[i]==x:
        print(i)
        break
else:
    print(f"{x} is not found")