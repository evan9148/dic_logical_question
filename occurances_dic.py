a = "MISSISSIPPI"
i=0
empty_dic = {}
while i<len(a):
    j=0
    count=0
    while j<len(a):
        if a[i] == a[j]:
            count=count+1
        j=j+1
    empty_dic[a[i]] = count
    i=i+1
print(empty_dic)
