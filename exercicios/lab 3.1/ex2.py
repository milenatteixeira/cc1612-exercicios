
# coding: utf-8

# In[1]:


n1 = float(input("digite o primeiro número:"))
n2 = float(input("digite o segundo número:"))

op = input("digite a operação: ")

if op == "soma":
    soma = n1+n2
    print("%.2f + %.2f = %d" % (n1, n2, soma))
elif op == "subtração":
    sub = n1-n2
    print("%.2f - %.2f = %d" % (n1, n2, sub))
elif op == "multiplicação":
    mult = n1*n2
    print("%.2f x %.2f = %d" % (n1, n2, mult))
elif op == "divisão":
    div = n1/n2
    print("%.2f / %.2f = %d" % (n1, n2, div))
else:
    print("A operação escolhida não é válida.")

