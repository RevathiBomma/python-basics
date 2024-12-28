def find_duplicate(arr):
    l=[]
    for num in arr:
        if num in l:
            return num
        l.append(num)
n=int(input("enter range"))
a=list(map(int,input().split()))
result=find_duplicate(a)
print(result)
        
        
