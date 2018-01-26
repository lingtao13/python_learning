s1 = '12345567'
s2 = 'abcdefg'

print(s1+s2)
print(str.__ge__(s1,s2))

pl = ["<0112>", "<32>", "<1204x768>", "<60>", "<1>", "<100.0>", "<500.0>"]
s = ''
for p in pl:
    s += p
print(s)
print(''.join(s))
print(''.join(str(x) for x in s))