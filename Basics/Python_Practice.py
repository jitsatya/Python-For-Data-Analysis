
# coding: utf-8

# Taking User Input and type conversion

# In[3]:


input(prompt = "Name: ")


# In[28]:


first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
result = int(first_number) + int(second_number)
print(result)


# User Input comes always in String format as it is universal format

# In[9]:


type(first_number)


# Two types of type conversion
# 1. Implicit : Python automatically converts
# 2. Explicit : Should be converted by programmer

# In[11]:


#Implicit
4 + 5.5


# In[12]:


5+6j


# In[16]:


#Explicit conversion
int('45')


# In[17]:


float(4)


# In[18]:


str(5)


# In[20]:


bool(1)


# In[21]:


complex(4)


# In[22]:


list('hello')


# type conversion is not parmanent

# In[24]:


a=4.5


# In[25]:


int(a)


# In[26]:


a # Original variable stays same


# In[29]:


first_number = int(input("Enter the first number: ")) # converting type when taking input
second_number = int(input("Enter the second number: "))
result = first_number + second_number
print(result)

