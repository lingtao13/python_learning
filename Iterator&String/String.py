

import re

'''s1=s.split(',')
s2 = re.split('[,;/|]+',s)
s2 = [x for x in s2 if x]

print(s1)
print(s2)
print(s)'''
def mySplit(s,ds):
    res = [s]
    print(res)
    for d in ds:
        t=[]
        list(map(lambda x:t.extend(x.split(d)),res))
        res = t
    return (x for x in res if x)
s = 'asd;qwe,qweesk2|3as|dqww qeefsav,qwef;aaaww,wdss/'

print(list(mySplit(s, ',;/|')))

print(re.split('[,;/|]+', s))
