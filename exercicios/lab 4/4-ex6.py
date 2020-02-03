
# coding: utf-8

# In[1]:


somatorio=0
contador=0

while True:
    num = int(input("Digite um número: "))
    somatorio = somatorio + num
    contador+=1
    if num==0:
        contador-=1
        print("A quantidade de números inseridos antes do 0 foi de %d"% contador)
        print("O somatório desses números inseridos é de %d"% somatorio)
        print("A média aritmética dos números inseridos é de %.2f"% (somatorio/contador))
        break

