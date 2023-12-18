#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Model.ipynb
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_and_evaluate_model(data):
    """
    Entraîne un modèle SVM linéaire sur les données fournies, évalue ses performances
    sur un ensemble de test et retourne le modèle, le vectoriseur, les données vectorisées
    de l'ensemble de test, et les étiquettes réelles de l'ensemble de test.

    Args:
    data (DataFrame): Les données, avec une colonne 'cleaned_text' contenant le texte nettoyé
                     et une colonne 'label' contenant les étiquettes.

    Returns:
    tuple: Un tuple contenant le modèle entraîné, le vectoriseur, les données vectorisées
           de l'ensemble de test, et les étiquettes réelles de l'ensemble de test.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        data['cleaned_text'], data['label'], test_size=0.2, random_state=42, stratify=data['label']
    )

    vectorizer = TfidfVectorizer()
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)

    model = SVC(kernel='linear')
    model.fit(X_train_vectorized, y_train)

    predictions = model.predict(X_test_vectorized)

    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy: {accuracy}")
    print(classification_report(y_test, predictions))

    return model, vectorizer, X_test_vectorized, y_test

def plot_confusion_matrix(model, X_test_vectorized, y_test):
    """
    Trace la matrice de confusion pour évaluer les performances du modèle.

    Args:
    model: Le modèle entraîné.
    X_test_vectorized: Les données vectorisées de l'ensemble de test.
    y_test: Les étiquettes réelles de l'ensemble de test.
    """
    predictions = model.predict(X_test_vectorized)
    conf_matrix = confusion_matrix(y_test, predictions)

    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.title('Matrice de Confusion')
    plt.xlabel('Prédictions')
    plt.ylabel('Réelles')
    plt.show()


# In[ ]:




