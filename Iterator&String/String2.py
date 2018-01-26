import os, stat

os.listdir(('.'))

s = [name for name in os.listdir('.') if name.endswith(('.sh','.py'))]

print(s)

print(oct(os.stat('String.py').st_mode))

os.chmod('String.py',os.stat('String.py').st_mode|stat.S_IXUSR)