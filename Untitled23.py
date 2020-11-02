#!/usr/bin/env python
# coding: utf-8

# In[1]:


skillsanta_dict={
    'name':'sachin',
    'age':20,
    'salary':2000,
    'city':'newdelhi'}
#old_key='city'
#new_key='location'
skillsanta_dict['location']=skillsanta_dict.pop('city')
print(skillsanta_dict)


# In[2]:


original_list=[11,45,8,11,23,45,23,45,89]
dict1={}
for i in original_list:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
print( dict1)


# In[3]:


def duplicate(samplelist):
    li=[]
    for i in samplelist:
        if i not in li:
            li.append(i)
    return li
samplelist=[87,45,41,65,94,41,99,94]
k=(duplicate(samplelist))
print(k)
s=tuple(k)
print(s)
print('min:',min(s))
print('max:',max(s))


# In[4]:


def showEmployee(name,salary=50000):
    print('employee {} salary is:{}'.format(name,salary))
showEmployee('Eddy',50000)
showEmployee('Eddy')


# In[5]:


def calculate(a,b):
    #square=a*4
    def addition(a,b):
       return a+b  
    add=addition(a,b)
    return  add+5
a=int(input('enter the number a:'))
b=int(input('enter the number b:'))      
result=calculate(a,b)
print(result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




