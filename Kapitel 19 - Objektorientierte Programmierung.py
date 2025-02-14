# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 02:15:59 2025

@author: danie
"""


""" Klassen:

Schlüsselwort: class
"""


class Beispielklasse:
    
    def __init__(self):
        self.name = "Dummyname"
        print("Eine neue Instanz wird erzeugt!")
    
    def bspFunktion(self,Name):
        self.name = Name
        return
        




""" Konstruktor:
Die Methode __init__ nennt man Konstruktor. Sobald eine neue Instanz einer Klasse
erzeugt wird, wird der Konstruktor automatisch aufgerufen. Dort wird die eigentliche 
Struktor der Klasse definiert.
"""

x = Beispielklasse()
x.name
x.bspFunktion("Danny")
x.name


""" Vererben:
Wiederverwendbarkeit von Code zu verbessern. Basisklasse vererbt ihre 
Fähigkeiten an eine Tochterklasse.  
"""

class neueKlasse(Beispielklasse):
    
    def __init__(self):
        self.nachname = "last name"
        print("Print von vererbterInstanz!")
        
    def bspFunktion2(self,Nachname):
        print("Hello")


obj1 = Beispielklasse()
obj2 = neueKlasse()


"""
Konstruktor der parentklasse UND neue in vererbter Klasse drinn haben:
"""


class neueKlasse2(Beispielklasse):
    
    def __init__(self):
        super().__init__() # Konstruktor aus Basisklasse
        self.nachname = "last name"
        print("Print von vererbterInstanz!")
        
    def bspFunktion2(self,Nachname):
        print("Hello")
        super().bspFunktion() # Methode aus Basisklasse
    
    
obj3 = neueKlasse2()





