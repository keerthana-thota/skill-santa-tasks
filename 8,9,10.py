#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
def validation(phone):
    pattern="^[6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$"
    return re.search(pattern,phone)
while True:
    phone=input('enter the number:')
#while True:
    if validation(phone):
        print(phone,"number is valid")
        break
    else:
        print(phone,"number is not valid")
    another=input('do u want enter valid number y/n:')
    if another=='y':
        continue
    else:
        break


# In[2]:


sample_string='The quick Brown Fox'
count=0
count1=0
for i in sample_string:
    if i.isupper():
        count=count+1
    elif i.islower():
        count1=count1+1
print('No.of Uppercase charcters:',count)
print('No.of Lowerrcase charcters:',count1)


# In[3]:


num=int(input('enter the number:'))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(num,'is a perfect number')
else:
    print(num ,'is not a perfect number')
        


# In[ ]:




