import pickle
f=open('studentPickle.dat','rb')
b=pickle.load(f)
b.displaystudent()
f.close()
