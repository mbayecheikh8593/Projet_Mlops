#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Preprocessing.ipynb

def clean_text(text):
    """
    Cette fonction prend en entrée un texte brut et applique plusieurs étapes de nettoyage pour le prétraiter.

    Paramètres :
    ---------------
    text : str
        Le texte brut à nettoyer.

    Retour :
    ---------------
    str
        Le texte nettoyé.

    Étapes de nettoyage :
    -------------------------
    1. Supprime la chaîne 'Subject:' du texte.
    2. Convertit le texte en minuscules.
    3. Supprime les caractères non alphabétiques, ne conservant que les lettres.
    4. Tokenise le texte en mots.
    5. Retourne le texte nettoyé après avoir supprimé les mots d'arrêt (stopwords) de la langue anglaise.

    Exemple :
    -----------------
    >>> text = "Subject: Hello, this is a sample text!"
    >>> clean_text(text)
    'hello sample text'
    """
    # Étape 1 : Supprimer la chaîne 'Subject:'
    text = re.sub(r'Subject:', '', text)

    # Étape 2 : Convertir en minuscules
    text = text.lower()

    # Étape 3 : Supprimer les caractères non alphabétiques
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    # Étape 4 : Tokeniser le texte
    tokens = word_tokenize(text)

    # Étape 5 : Supprimer les mots d'arrêt
    cleaned_text = ' '.join([word for word in tokens if word not in stopwords.words('english')])

    return cleaned_text

