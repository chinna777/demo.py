import pickle,PickeFile
f=open('studentPickle.dat','wb')
s=PickeFile.Student(1,'danny',100)
pickle.dump(s,f)
f.close()
