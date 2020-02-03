
# coding: utf-8

# In[1]:


x = float(input("digite a coordenada 'x':"))
y = float(input("digite a coordenada 'y':"))

if x>0 and y>0:
    print("Q1.")
elif x>0 and y<0:
    print("Q4.")
elif x<0 and y>0:
    print("Q2.")
elif x<0 and y<0:
    print("Q3.")
elif x==0 and (y<0 or y>0):
    print("está sobre o eixo das abscissas.")
elif (x<0 or x>0) and y==0:
    print("está sobre o eixo das coordenadas.")    
else:
    print("origem.")

