import logging
logging.basicConfig(filename='myfile.log',level=logging.DEBUG)
try:
    
    logging.info("entering the required inputs")
    a,b=[int(x) for x in input('enter the two numbers:' ).split()]
    f=open("myfile.py","w")
    c=a//b
    print(c)
    f.write('writing %d into myfile'%c)
    logging.info("writing the output to the file")
except ZeroDivisionError:
    logging.critical("not be divisble by zero ")
    print('division by zero is not applicable')
    print('please enter the non zero value')
else:
    print('madda gudu')
finally:
    f.close()
    print('file is closed')
   