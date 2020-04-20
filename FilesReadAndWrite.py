f=open("myAss1hey my ass.txt","w")
print("enter the data to be stored (Type @ at the end of yourb data but not anywhere in the middle)")

m=''
while m != '@' :
    m=input()
    f.write(m + '\n')


f.close()
