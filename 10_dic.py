i=0
empty_dic = {}
while i<=1:
    name = input("enter your name")
    age = int(input("enter your age"))
    empty_dic[name]=age
    i=i+1
print(empty_dic)
for i in empty_dic.items():
    print(i)
