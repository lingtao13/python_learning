# -*- coding: UTF-8 -*-
#生成一个函数传导出所有素数

'''def f():
    print ('in f(), 1') 
    yield 1

    print ('in f(), 2')
    yield 2

    print('in f(), 3')
    yield 3

g=f()

print(g)'''

class PrimeNumbers:
    def __init__(self,start,end):
        self.start=start
        self.end = end

    def isPrimeNum(self,k):
        for i in range(2,k):
            if k % i ==0:
                return False
        return True
    def __iter__(self):
        for k in range(self.start,self.end+1):
            if self.isPrimeNum(k):
                yield k

for x in PrimeNumbers(1,100):
    print(x)
