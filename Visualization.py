#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Visualization.py

import matplotlib.pyplot as plt
from collections import Counter

def plot_label_distribution(data):
    """
    Affiche un histogramme de la répartition des labels (Spam vs Non-Spam).

    Args:
    data (pd.DataFrame): Le DataFrame contenant les données.

    Returns:
    None
    """
    label_counts = data['label'].value_counts()
    plt.figure(figsize=(6, 4))
    label_counts.plot(kind='bar', color=['blue', 'orange'])
    plt.title('Répartition des labels (Spam vs Non-Spam)')
    plt.xlabel('Label')
    plt.ylabel('Nombre de mails')
    plt.xticks(rotation=0)
    plt.xticks(ticks=[0, 1], labels=['Non-Spam', 'Spam'])
    plt.show()

def plot_word_frequency(data, num_words=10):
    """
    Affiche un histogramme des mots les plus fréquents dans le corpus.

    Args:
    data (pd.DataFrame): Le DataFrame contenant les données.
    num_words (int): Le nombre de mots à afficher dans l'histogramme.

    Returns:
    None
    """
    corpus = ' '.join(data['cleaned_text'])
    word_freq = Counter(corpus.split())
    common_words = dict(word_freq.most_common(num_words))

    plt.figure(figsize=(10, 6))
    plt.bar(common_words.keys(), common_words.values(), color='blue')
    plt.title('Mots les plus fréquents')
    plt.xlabel('Mots')
    plt.ylabel('Fréquence')
    plt.show()


# In[ ]:




