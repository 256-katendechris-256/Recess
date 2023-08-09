import sys
from os.path import exists

script,f1,f2v=sys.argv
#opening one file
tar=open(f1)
gar=tar.read()

#opening the second one where all details are to be copied
zar =open(f2v,'w')
zar.write(gar)

print ("Welcome to the new age and also everything is radioactive")
zar.close()