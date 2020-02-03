
# coding: utf-8

# In[1]:


letra = input("digite uma letra qualquer: ")

if letra == "a":
    print("letra %s: vogal" % letra)    
elif letra == "e":
    print("letra %s: vogal" % letra)
elif letra == "i":
    print("letra %s: vogal" % letra)
elif letra == "o":
    print("letra %s: vogal" % letra)
elif letra == "u":
    print("letra %s: vogal" % letra)
elif letra == "y":
    print("É possível que a letra %s seja uma vogal ou uma consoante, dependendo da lingua." % letra)
else:
    print("letra %s: consoante" % letra)

