dic = [
    {"first":"2"}, 
    {"second": "1"}, 
    {"third": "2"}, 
    {"four": "5"}, 
    {"five":"5"}, 
    {"six":"9"},
    {"seven":"7"}
]
empty_list = []
for i in dic:
    for j in i:
        if i[j] not in empty_list:
            empty_list.append(i[j])
print(empty_list)