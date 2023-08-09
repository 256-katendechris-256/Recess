#===================================================LISTS================================================
#list of names
names = ['Katende', 'Chris','Marvin','Luffy','Optimus']
print(names[1])


# change value of the first item
names[0] = "Jonathan" 
print(names[0])


# add an item to end of list (append)
names.append("Joseph") # adds Joseph at last position in a list
print('Names: ', names)

#inserting a new name at the 3rd position on the list
names.insert(2, "Naruto")
print('Names after inserting Naruto: ', names)

# remove 4th item   from lists using pop() method
del names[3]    
print('Names after deleting Luffy : ', names)

#using negative indexing to print last item
print('Last Item is:', names[-1])

#using range to print items
anime=['AOT','Food_Wars','Naruto','Death_Note','Devil_as_a_part_timer','Kimetsu_No_yoiba','One_Piece']
print(anime[:5][2:])

#list of countries and make a copy of it
countries= ["Uganda","Tanzania", "Rwanda"]
copy_of_country=[]
for country in countries:
    copy_of_country.append(country)
    print(copy_of_country)

#loop through the countries list with for loop
for i in countries:
  print(i)
  
#sort list in ascending order
animals=['monkey','elephant','snake','lion']
sorted_animals= sorted(animals)
print(sorted_animals)

#sort list in descending order
animals=['monkey','elephant','snake','lion']
reversed_animals= reversed(animals)
print(reversed_animals)

#animals with 'a' in them
animals=['monkey', 'elephant', 'snake', 'lion']
filtered_animals=[x for x in animals if 'a' in x ]
print(filtered_animals)

#joining two lists
list1=["katende","Mutyaba"]
list2=['chris','bryan']
joined = list1+list2
print(joined)


#==================================TUPLES===============================================
x=("sumsang","iphone", "tecno","redmi")
print(x[0])

#second last item in tuple
print(x[-2])

#updating tuples
#first turn it into a list since its immutable
y =list(x)
y[1]="itel"
#then turnit back to a tuple
x=tuple(y)
print(x)

#adding a new item in tuple
x +=  ('Huawei',)
print(x)

#removing an existing item from the tuple
a =list(x)
a.remove('redmi')
x=tuple(a)
print(x)

#loop through a tuple
for i in range (len(x)):
   print(i,": ",x[i],)

#using the tuple constructor 
t=['kampala','masaka','matuga']  
tapo=tuple(t)
print(type(tapo))
print(tapo)

#unpack tuple
tup=('Kampala','Masaka','Matuga','luweero','Mbarara','gulu')
city,city1,city2,city3,city4,city5=tup
print(city)
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)


#range in tuples
cities=('Kampala','Masaka','Matuga','luweero','Mbarara','gulu')
selected=cities[2:5]
print("Selected Cities are", selected)

#adding two tuples
a=("katende","Mutyaba")
b=("chris","marvin")
u=list(a)
v=list(b)
e=u+v
c=(tuple(e))

print('The new list is', c)


 #multiplying a tuple by 3
x= ("kampala",'masaka',"matuga")
z = x*3
print(z)

#number of times 8 appears in the tuple
thistuple = (1,3,7,8,7,5,4,6,8,5)
count = thistuple.count(8)
print(f"Number of time 8 is: {count}")
      

#===============================================SETS==========================================================================
list=['pepsi','sprite','oner']
my_set= set(list)

print(my_set)

#add 2 more items to the set
my_set.update(['coke','mirinda'])

print(my_set)

myset={"oven","microwave","kettle","refrigerator"}
#check if refrigerator exists
if "refrigerator"in myset :
    print("Yes it does exist!")
else:
    print("No such item found.")    

#remove kettle from the set
myset.discard("kettle")
print(myset)

#loop through the set and display each element using for loop
for i in myset:
  print(i)

list= [34,56]  
set={'boy','girl','man','dog'}

#adding list items to set items
new_set=set.union(list) 

print(new_set)

#adding two sets together
set_A={10,9}
set_B={'Trevour','Steven'}
combined_set=set_A|set_B
print(combined_set)

#===================================STRINGS========================================================
a=90
b="Merry"
#concatinate a string and an integer value
c=str(a)+ b
print(c)

#output without spaces at the beginning, in the middle and the end
tst="  Hello,Uganda!         "
print (tst.lstrip())

#remove spaces in the middle
print ("\n"+ tst.rstrip() + "\n")

#convert tst to uppercase
print(tst.upper())


#replace U with  V
print("\n"+tst.replace('U', 'V'))


#return a range of characters in he 2nd 3rd and 4th position
y="I am proudly Ugandan"
print("\n"+y[1:4])

y ="Data Scientists"
x=f"All {y} are cool!"
print(x)

#=================================DICTIONARIES===============================================================
shoes={
   "brand":"Nike",
   "color":"black",
   "size":40

}
print("The shoe size is "+ str(shoes["size"]))

#change Nike to adidas
shoes['brand']='adidas'
print('\n'+str(shoes))

#add key/value to the dictionary
shoes['type']="sneakers"
print('\n'+str(shoes))

#return olny keys from dictionay
keys = shoes.keys()
print ('\n The Keys are '+str(keys))

#return only values form dictonary
values =shoes.values()
print ('\n Values are '+str(values))

#check if the key "size" exists
if'size'in shoes :
    print('Yes')
else:
    print('No')

#loop through the dictionary
for k,v in shoes.items():
    print (k+"="+str(v))

#remove color from dictionary
del shoes ['color']
print ("\n"+str(shoes))



#empty the dictionary
shoes={}
print("\n"+str(shoes))

#make copy of dictionary
dict={
   "one":1,"two":2,"three":3}

copy=dict.copy()
print("\n"+str(copy))

#nested dictionaries
d={'a':{'b':'c'}}
print("\n"+ str(d))




