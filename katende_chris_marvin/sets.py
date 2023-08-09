#using strings
set1 =set("KATENDE")
print(set1)

#using a list
set2 =set(["one","two","three","four","one"])
print(set2)

#using curly braces
set3={1,2,3,4,5,6}

#1. length of a set
arc =set2.__len__()
print(arc)
#or
print(len(set3))

#2.datatype contained in set
print(type(set3))

set4 ={"katende",23,27.0,"chris"}
data_types=set()
for el in set4:
    data_types.add(type(el))

print(data_types)

#3.Accessing a set
set5={"Little","wait",34,89.6}

    #using the for loop
for i in set5:
    print(i)    

    #using the in keyword
print(34 in set5)    

#4. Adding elements in a set
set5.add(3)

    #adding tupples in a set
set5.add((2,34,56))
print(set5)
    #using an iterator
for i in range(20,73):
    set3.add(i)
print(set3)   

#union of two sets
set6 ={1, 2 ,3 }
set7 = {3, 4 ,5 }
set8 = set6 | set7
print("Union is : ",set8)

#intersection of two sets
set9 = {1, 2 ,3 }
set10 = {3, 4 ,5 }
set11 = set9 & set10
print("Intersection is : ",set11)