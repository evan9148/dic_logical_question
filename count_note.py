salary=int(input("enter your salary"))
notes=int(input("enter your note"))
if notes==500:
    print(salary//500,"notes are there in",salary)
elif notes==100:
    print(salary//100,"notes are there in",salary)
elif notes==50:
    print(salary//50,"notes are there in",salary)
else:
    print("nothing")
