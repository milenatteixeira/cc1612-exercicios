from random import randint, uniform
inteiros = []
reais = []
strings = ["a","b","c","d","e","f","g"]
complexos = [9+2j,7-8j,1+2j,2-6j,1-2j]
for i in range(10):
    num = randint(0,100)
    inteiros.append(num)

for i in range(15):
    num = round(uniform(0,100),2)
    reais.append(num)

completa = [inteiros, reais, strings, complexos]

inteiros,reais,strings,complexos = [],[],[],[]

print("             PRIMEIRA LISTA COMPLETA               ")
print(completa)
print("                            ")
print("                            ")
for i in range(50):
    num = randint(0,100)
    completa[0].append(num)
print("             SEGUNDA LISTA COMPLETA               ")
print(completa)
