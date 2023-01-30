mylist=['apple',123,'pink',124.56]
print(mylist)
# find length of list by using len() method 
print(len(mylist))
#to find the data type of list by using type ()
print(type(mylist))
#access list item
p=mylist[0]
print(p)
# p= mylist[4] #list index out of range
# print(p)
print(mylist)
p=mylist[-2]
print(p)
mylist.append(123)
print(mylist)
mylist2=[1,2,5,6]
mylist2.extend(mylist)
print(mylist2)
mylist2.insert(2,10)
print(mylist2)
del mylist2[2] #by using del we can delete specific element from the list
print(mylist2)
mylist2.clear()
print(mylist2)
