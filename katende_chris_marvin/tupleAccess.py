# tuples are immutable and ussually, 
"""type they contain a sequence of heterogeneous
 elements that are accessed via unpacking or indexing"""


#1. using tuple indexing
tapo =("Katende","chris","marvin")
print(tapo[2])

#2.  using tuple unpacking
a, b, c =tapo
print(a)
print(b)
print(c)

#3. using the len() metod in tuples
    # use the __len__() instead of len()
print(tapo.__len__())


#4. counting repeated values in  a tuple
tapo2= (2,5,3,2,7,9,2,6,2,2,5)
print(tapo2.count(2))

#5. deleting a tuple
tapo1=(1,2,3,4,4)
print(tapo1)
#del tapo1
#print(tapo1)


#6. slicing of a tuple
tapo3 =tuple('KATENDE') 
print(tapo3[0:])
