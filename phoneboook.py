# class making object phonebook in memory.
class phonebook :
    def __init__(self,name,phonenumber) :
        self.name = name
        self.phonenumber = phonenumber
# empty list for saving objects.
list1=[]
# count = number of new enteries user want to input in the data details.
count=int(input("number of enteries :- "))
for i in range(count) :
    x,y=input(f"{i+1}:) name :- "),int(input(f"   number :- "))
    list1.append(phonebook(x,y))
# empty list for saving names for query.
list_query=[]
# count = number of new queries user want to check in the data details.
count=int(input("number of queries :- "))
for i in range(count) :
    x=input(f"{i+1}:)name :- ")
    list_query.append(x)
for j in list_query :
    flag=False
    for k in range(len(list1)):
        if j==list1[k].name :
            print(f"{list1[k].name}={list1[k].phonenumber}")
            flag=True
    if flag==False :
        print("not found")