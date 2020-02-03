
# coding: utf-8

# In[1]:


dia = int(input("digite a quantidade de dias: "))
diaConvertido = dia*24*60*60
hr = int(input("digite a quantidade de horas: "))
hrConvertido = hr*60*60
minutos = int(input("digite a quantidade de minutos: "))
minutosConvertido = minutos*60
seg = int(input("digite a quantidade de dias: "))

soma = diaConvertido+hrConvertido+minutosConvertido+seg

print("Os %d dias, %d horas, %d minutos e %d segundos é: %d" % (dia,hr,minutos,seg,soma))

