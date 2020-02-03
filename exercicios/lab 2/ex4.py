
# coding: utf-8

# In[1]:


salHora = float(input("digite o quanto voce ganha por hora: "))
horas = int(input("digite quantas horas por mês: "))

salarioBruto = salHora * horas

print("+ Salário Bruto: R$%.2f"% (salarioBruto))

salarioIR = (salarioBruto * 0.11)

print("- Imposto de Renda (11%%): R$%.2f"% (salarioIR))

salarioINSS = (salarioBruto * 0.08)

print("- INSS (8%%): R$%.2f"% (salarioINSS))

salarioS = (salarioBruto * 0.05)

print("- Sindicato (5%%): R$%.2f"% (salarioS))

salarioL = salarioBruto-salarioIR-salarioINSS-salarioS

print("= Salário Liquido : R$%.2f"% (salarioL))

