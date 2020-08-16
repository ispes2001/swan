# import datetime

# present = datetime.datetime.now()
# offerenddate = datetime.datetime(2020, 11, 25, 8, 0, 0)
# countdown = offerenddate - present
# print(countdown.seconds)


class A:
    def process(self):
        print('A process()')


class B:
    pass


class C(A, B):
    pass


# obj = C()  
# obj.process()    
print(C.mro())   # print MRO for class C
