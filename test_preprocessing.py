#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest from preprocessing import clean_text class TestPreprocessing(unittest.TestCase): 
    def test_clean_text(self): # Testez la fonction de nettoyage sur un exemple spécifique 
        input_text = "Hello! This is a sample email text. Subject: Important" 
        expected_output = "hello sample email text" 
        self.assertEqual(clean_text(input_text), expected_output) # Ajoutez d'autres cas de test en fonction de vos besoins 
        if __name__ == '__main__': unittest.main()

