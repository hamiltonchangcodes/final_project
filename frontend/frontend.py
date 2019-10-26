#!/usr/bin/env python
# coding: utf-8

# In[7]:


from PIL import Image


# In[2]:


import streamlit as st
import numpy as np
import pandas as pd


# In[9]:


st.title('Yelp Report Card')


# In[10]:


st.write('by Hamilton Chang\n')


# In[11]:


image = Image.open('download.png')
st.image(image, caption='Yelp!', use_column_width=False, format='PNG')


# In[12]:


st.markdown('Welcome to the Yelp Report Card.  For this project, I collected approximately 115,000 reviews from 896 restaurants in New York City.  I then processed them for Sentiment Analysis to determine if the review was positive or negative.  My next step was to use Latent Dirichlet Alloction or LDA on the approximately 3.7 million words in the reviews to determine the topic of the review, separated as Food, or Service.  Lastly, I combined my two analysis to determine if the reveiwer liked the food/service, or did not like the food/service and produced a final score as a percentage of responses.')


# In[13]:


st.markdown('Why are we doing this?  To help restaurants establish a baseline and determine what part of the dining experience they need to work on.  This potentially could be an add on service for business owners so they can fine tune their restaurant and hopefully improve their numbers.')


# In[14]:


st.markdown('## Feel Free to Play with it!')


# In[22]:


df1 = pd.read_csv('displaycardManhattan.csv')


# In[23]:


df1 = df1.set_index('restaurant')


# In[26]:


df1 = df1.drop(columns='Unnamed: 0')


# In[24]:


named = df1.index.to_list()


# In[ ]:


option = st.sidebar.selectbox(
    'Choose a Restaurant',
     named)


# In[8]:


st.balloons()


# In[ ]:


st.write(df1.loc[option])


# In[9]:


st.bar_chart(df1.loc[option], height=40)


# In[3]:


number = st.number_input('give me a number!')
st.write('you chose', number)


# In[ ]:




