try :
    n=int(input("enter the required num :"))
    assert n%2==0, 'please enter the even number'
    print('you are  good to go')
except AssertionError as hmm:
    print(hmm)
    print('hey check youer error message')
