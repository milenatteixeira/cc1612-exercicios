n = int(input('digite um número: '))
m = int(input('digite outro número: '))
d=0

if n>m:
    d = m
else:
    d = n

while m%d!=0 or n%d!=0:
    d-=1
print(d)
    
