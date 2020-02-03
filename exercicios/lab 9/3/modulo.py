dic = {}

x = input("digite uma string: ")
cont = 0

for i in x:
    dic[i] = 1
dic = list(dic)

print(x)
print(dic)
print(len(dic))
