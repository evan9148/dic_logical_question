my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20,
}
a=[]
highest=0
sec_highest=0
third_highest=0
for i in my_dict:
    for j in my_dict:
        if highest<my_dict[j]:
            highest=my_dict[j]
        elif highest>my_dict[j] and sec_highest<my_dict[j]:
            sec_highest=my_dict[j]
        elif sec_highest>my_dict[j] and third_highest<my_dict[j]:
            third_highest=my_dict[j]
a.append(highest)
a.append(sec_highest)
a.append(third_highest)
print(a)

