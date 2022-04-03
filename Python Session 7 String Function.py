#!/usr/bin/env python
# coding: utf-8

# # String Functions

# In[16]:


firstname="Santhosh Kumar"


# In[18]:


firstname.upper()


# In[ ]:


Last_Name="Mahalingam"


# In[19]:


Last_Name


# In[21]:


Last_Name.lower()


# In[22]:


city="Pune"


# In[23]:


City1=city.lower()


# In[24]:


City1


# In[26]:


b="LeNoVo"


# In[27]:


b


# In[30]:


b.swapcase()


# In[31]:


M="SaNtHoSh"


# In[32]:


M.swapcase()


# In[33]:


val="I am learning Data Science"


# In[34]:


val.split()


# In[35]:


string1="conmputer"


# In[36]:


string1.isupper()


# In[37]:


string1.islower()


# In[38]:


string1.isalpha()


# In[40]:


string1.isnumeric()


# In[42]:


string1.isdigit()


# In[45]:


S="ABCD1234"


# In[46]:


S.isalnum()


# In[48]:


T="tamilnadu"


# In[49]:


T.capitalize()


# In[50]:


Val="i am learning data science"


# In[51]:


val.title()


# In[53]:


string1="Santhosh"
string2="SaNtHoSh"
if string1.casefold()==string2.casefold():
    print("Match is correct")
else:
    print("Match is incorrect")


# In[54]:


name="John"
print("Hello,%s!"%name)


# In[63]:


name="john"
age=55
print('%s is %d years old' % (name, age))


# In[64]:


name="sam"


# In[65]:


age=24


# In[67]:


print('He is {} and he is {} years old'.format(name,age))


# In[ ]:





# In[ ]:




