list1=[3,2,1,4,5,6]
print(list1)

list2 =["jake", 7, "emmily",8]
print(type(list2))

print(len(list2))
print(list2[-2])
#access in range
print(list1[0:3])

#methods
"""append   adds item at the end of the list
   remove    removes that particular item from the list 
   insert   adds an item at a given location/ index
   pop    uses an idex to delete
"""
list1.append(7)
print(list1)
list1.insert(0,"hey")
print(list1)
list1.pop(0)
print(list1)