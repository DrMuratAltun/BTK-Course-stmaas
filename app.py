#!/usr/bin/env python
# coding: utf-8

# # Maaş Tahmin eden bir web uygulaması

# In[1]:


#pip install streamlit


# In[4]:


import streamlit as st
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore")


# In[5]:


st.title("Maaş Tahmin Sistemi:heavy_dollar_sign:")


# In[6]:


model = pickle.load(open("model.pkl", "rb"))
tecrube=st.number_input("Tecrube",1,10)
yazili=st.number_input("Sınav",1,10)
mulakat=st.number_input("Mulakat",1,10)
if st.button("Tahmin Et"):
    tahmin=model.predict([[tecrube,yazili,mulakat]])
    tahmin=round(tahmin[0],2)
    st.write(f"Tahmin Edilen Maas $: {tahmin}")


# In[ ]:




