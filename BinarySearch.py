pos=-1

def search(l1,n):
    l=0,
    u=len(l1)-1

    while  l<=u :
        midpoint = (l+u) // 2
        if l1[midpoint]==n:

            # globals() ['pos']=midpoint
            return True
        else:
            if n>midpoint:
            
                l=midpoint
            elif n<midpoint: 
                u=midpoint
            else:
                n!= (x for x in l1)
            print('element not found')
l1=[22,77,7,4,5,6,26,54]
n=int(input('enter the number :'))

search(l1,n)






