# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv 
liste_nom = ['b', 'c', 'a', 'f']
table_grade= {'Id_Grade': 1 ,'Nom' : liste_nom  , 'Type' : 'haut' , 'Libelle': ' grade' }

with open(r"C:\Users\g25002725\Downloads\Tableurs Tenrac Final.xlsx", mode='r', newline='') as fichier:
    lecteur = csv.reader(fichier)
    print(table_grade['Nom'])
        
        
        
import pandas as pd

fichier_excel = pd.ExcelFile(r"C:\Users\g25002725\Downloads\Tableurs Tenrac Final.xlsx")

# Affiche la liste des noms de feuilles
print(fichier_excel.sheet_names) 

# Exemple : Boucler sur toutes les feuilles pour les lire
for nom_feuille in fichier_excel.sheet_names:
    df = pd.read_excel(fichier_excel, sheet_name=nom_feuille)
    print(f"Chargement de la feuille : {nom_feuille}")