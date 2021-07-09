#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


n_sample=100000


# In[3]:


df1=pd.read_csv("BOUN_TCP_Anon.csv",nrows=n_sample)


# In[11]:


df2=pd.read_csv("BOUN_UDP_Anon.csv",nrows=n_sample)


# In[12]:


df=pd.concat([df1,df2],axis=0,ignore_index=True)


# In[ ]:


df.head()


# In[ ]:


df['TCP_Protocol'].value_counts()


# In[ ]:


df['Source_ip'].value_counts()


# In[ ]:


l=['10.50.197.71','10.50.192.199']


# In[ ]:


print(df)


# In[ ]:


for i in range(0,len(df)):
    if(df['Source_ip'][i] not in l):
        df['Source_ip'][i]='other_src_ip'
src_dummies=pd.get_dummies(df['Source_ip'])
src_dummies=src_dummies.rename(columns={"10.50.197.71":"src_71","10.50.192.199":"src_199"})


# In[ ]:


src_dummies.head()


# In[ ]:


df_new=src_dummies


# In[ ]:


df['Destination_IP'].value_counts()


# In[ ]:


l1=['10.50.197.71','10.50.192.199']


# In[ ]:


for i in range(0,len(df)):
    if(df['Destination_IP'][i] not in l1):
        df['Destination_IP'][i]='other_dest_ip'
dst_dummies=pd.get_dummies(df['Destination_IP'])
dst_dummies=dst_dummies.rename(columns={"10.50.197.71":"dst_71","10.50.192.199":"dst_199"})


# In[ ]:


df_new=pd.concat([df_new,dst_dummies],axis=1)


# In[ ]:


for i in range(0,len(df)):
    if(pd.isnull(df['Source_Port'][i])):
        df['Source_Port'][i]=-1;


# In[9]:


df['Source_Port'].value_counts()


# In[8]:


for i in range(0,len(df)):
    if(pd.isnull(df['Destination_Port'][i])):
        df['Destination_Port'][i]=-1;


# In[7]:


df['Destination_Port'].value_counts()


# In[6]:


for i in range(0,len(df)):
    if(pd.isnull(df['SYN'][i])):
        df['SYN'][i]="NaN";


# In[4]:


for i in range(0,len(df)):
    if(pd.isnull(df['ACK'][i])):
        df['ACK'][i]="NaN"


# In[5]:


for i in range(0,len(df)):
    if(pd.isnull(df['RST'][i])):
        df['RST'][i]="NaN";


# In[98]:


df['SYN'].value_counts()


# In[99]:


df['ACK'].value_counts()


# In[100]:


df['RST'].value_counts()


# In[101]:


for i in range(0,len(df)):
    if(df['Source_Port'][i]==-1):
        df['Source_Port'][i]='srcport_null'
    elif(df['Source_Port'][i]==443):
        df['Source_Port'][i]='srcport_443'
    elif(df['Source_Port'][i]==49543):
        df['Source_Port'][i]='srcport_49543'
    else:
        df['Source_Port'][i]='other_srcport'
        
    if(df['Destination_Port'][i]==-1):
        df['Destination_Port'][i]='dstport_null'
    elif(df['Destination_Port'][i]==443):
        df['Destination_Port'][i]='dstport_443'
    elif(df['Destination_Port'][i]==49543):
        df['Destination_Port'][i]='dstport_49543'
    else:
        df['Destination_Port'][i]='other_dstport'


# In[102]:


srcport_dummies=pd.get_dummies(df['Source_Port'])
dstport_dummies=pd.get_dummies(df['Destination_Port'])


# In[103]:


df_new=pd.concat([df_new,srcport_dummies],axis=1)


# In[104]:


df_new=pd.concat([df_new,dstport_dummies],axis=1)


# In[105]:


for i in range(0,len(df)):
    if(df['SYN'][i]=='Not set'):
        df['SYN'][i]="SYN_NOT_SET"
    else:
        df['SYN'][i]="SYN_Other"
        
    if(df['ACK'][i]=="Set"):
        df['ACK'][i]="ACK_SET"
    else:
        df['ACK'][i]="ACK_Other"
        
    if(df['RST'][i]=='Not set'):
        df['RST'][i]="RST_NOT_SET"
    else:
        df['RST'][i]="RST_Other"


# In[106]:


syn_dummies=pd.get_dummies(df['SYN'])
ack_dummies=pd.get_dummies(df['ACK'])
rst_dummies=pd.get_dummies(df['RST'])


# In[107]:


syn_dummies.head()


# In[108]:


ack_dummies.head()


# In[109]:


rst_dummies.head()


# In[110]:


df['TTL'].value_counts()


# In[111]:


df_new=pd.concat([df_new,syn_dummies],axis=1)


# In[112]:


df_new=pd.concat([df_new,ack_dummies],axis=1)


# In[113]:


df_new=pd.concat([df_new,rst_dummies],axis=1)


# In[ ]:




