#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Preprocessing.ipynb

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def clean_text(text):
    text = re.sub(r'Subject:', '', text)
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    tokens = word_tokenize(text)
    cleaned_text = ' '.join([word for word in tokens if word not in stopwords.words('english')])
    return cleaned_text

