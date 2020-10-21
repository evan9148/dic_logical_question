list1 = [2,3,2,4,10,3,3,4]
i=0
while i<len(list1):
    j=0
    a=[]
    count=0
    while j<len(list1):
        if list1[i] == list1[j]:
            count=count+1
        j=j+1
    a.append(list1[i])
    a.append(count)
    i=i+1
    print(a)
