#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo(n-1) + fibo(n-2))  
n = int(input())  
if n <= 0:  
   print("Wrong input")  
else:  
   print("Fibonacci sequence:")  
   for i in range(n):  
       print(fibo(i))


# In[3]:


def displayStudent(name,age):
    print(name,age)
displayStudent('chotu',25)
showStudent=displayStudent
showStudent('chotu',25)


# In[ ]:





# In[ ]:





# In[ ]:




