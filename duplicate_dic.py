dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "2":"fdgggh",
    "bat":3
    }
empty_dic={}
for i in dic:
    if i not in empty_dic:
        empty_dic.update(dic)
print(empty_dic)

