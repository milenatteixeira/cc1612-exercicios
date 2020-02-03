
# coding: utf-8

# In[1]:


dia = int(input("digite o dia:"))
mes = int(input("digite o mes:"))
ano = int(input("digite o ano:"))
print("")
print("%d/%d/%d" %(dia,mes,ano))
print("")

if mes==1:
    if dia == 31:
        dia = 1
        mes+=1
        print("%d/%d/%d" %(dia,mes,ano))
    else:
        dia+=1
        print("%d/%d/%d" %(dia,mes,ano))
elif mes==2:
    if (ano%400==0) or ((ano%4==0)and(ano%100!=0)):
        if dia==29:
            dia = 1
            mes +=1
            print("%d/%d/%d" %(dia,mes,ano))
        else:
            dia+=1
            print("%d/%d/%d" %(dia,mes,ano))
    else:
        if dia==28:
            dia = 1
            mes +=1
            print("%d/%d/%d" %(dia,mes,ano))
        else:
            dia+=1
            print("%d/%d/%d" %(dia,mes,ano))
elif mes==3:
    if dia==31:
        dia = 1
        mes +=1
        print("%d/%d/%d" %(dia,mes,ano))
    else:
        dia+=1
        print("%d/%d/%d" %(dia,mes,ano))
elif mes==4:
    if dia==30:
        dia = 1
        mes +=1
        print("%d/%d/%d" %(dia,mes,ano))
    else:
        dia+=1
        print("%d/%d/%d" %(dia,mes,ano))
elif mes==5:
    if dia==31:
        dia = 1
        mes +=1
        print("%d/%d/%d" %(dia,mes,ano))
    else:
        dia+=1
        print("%d/%d/%d" %(dia,mes,ano))
elif mes==6:
    if dia==30:
        dia = 1
        mes +=1
        print("%d/%d/%d" %(dia,mes,ano))
    else:
        dia+=1
        print("%d/%d/%d" %(dia,mes,ano))
elif mes==7:
    if dia==31:
        dia = 1
        mes +=1
        print("%d/%d/%d" %(dia,mes,ano))
    else:
        dia+=1
        print("%d/%d/%d" %(dia,mes,ano))
elif mes==8:
    if dia==31:
        dia = 1
        mes +=1
        print("%d/%d/%d" %(dia,mes,ano))
    else:
        dia+=1
        print("%d/%d/%d" %(dia,mes,ano))
elif mes==9:
    if dia==30:
        dia = 1
        mes +=1
        print("%d/%d/%d" %(dia,mes,ano))
    else:
        dia+=1
        print("%d/%d/%d" %(dia,mes,ano))
elif mes==10:
    if dia==31:
        dia = 1
        mes +=1
        print("%d/%d/%d" %(dia,mes,ano))
    else:
        dia+=1
        print("%d/%d/%d" %(dia,mes,ano))
elif mes==11:
    if dia==30:
        dia = 1
        mes +=1
        print("%d/%d/%d" %(dia,mes,ano))
    else:
        dia+=1
        print("%d/%d/%d" %(dia,mes,ano))
elif mes==12:
    if dia==31:
        dia = 1
        mes = 1
        ano+=1
        print("%d/%d/%d" %(dia,mes,ano))
    else:
        dia+=1
        print("%d/%d/%d" %(dia,mes,ano))

