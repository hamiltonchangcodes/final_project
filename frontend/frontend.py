#!/usr/bin/env python
# coding: utf-8

# In[18]:


from PIL import Image


# In[19]:


import streamlit as st
import numpy as np
import pandas as pd


# In[20]:


st.title('Yelp Report Card')


# In[ ]:


st.write('by Hamilton Chang\n')


# In[21]:


image = Image.open('download.png')
st.image(image, caption='Yelp!', use_column_width=False, format='PNG')


# In[28]:


st.markdown('Welcome to the Yelp Report Card.  For this project, I collected approximately 115,000 reviews from 896 restaurants in New York City.  I then processed them for Sentiment Analysis to determine if the review was positive or negative.  My next step was to use Latent Dirichlet Alloction or LDA on the approximately 3.7 million words in the reviews to determine the topic of the review, separated as Food, or Service.  Lastly, I combined my two analysis to determine if the reveiwer liked the food/service, or did not like the food/service and produced a final score as a percentage of responses.')


# In[ ]:





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


# In[ ]:




