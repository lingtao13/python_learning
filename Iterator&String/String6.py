s = '     avs    123    sss   '
print(s.strip())
s1 = '---abc+++'
print(s1.strip('+-'))   #删除两端

s2='abc:123'
print(s2[:3]+s2[4:])    #切片操作

s3='\ta\r\nbc\t12\r\n3\txyz'
print(s3.replace('\t',''))

import re

print(re.sub('[\t\r\n]','',s3))


print(s3.translate(str.maketrans('abcxyz','xyzabc')))   #str 变成基础库，不需要导入string了

