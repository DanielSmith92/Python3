# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 01:21:38 2025

@author: Daniel Smith
"""

"""
Kapitel 7: Das Datenmodell

Kernidee des Kapitels: Wie verwaltet Python Daten zur Laufzeit?
Stichwörter: Objekt, Instanz, Referenz

- Instanz: Ein konkretes Datenobjekt im Speicher, das nach der Vorlage eines 
           bestimmten Datentyps erzeugt wurde. Jede Instanz umfasst 3 Komponenten:
               Datentyp, Wert, Identität

- Referenz: Eine Referenz ist ein 'Verweis' auf eine Instanz. Referenzen machen
            es uns möglich auf Instanzen zugreifen zu können. Mit dem Zuweisungsoperator (=)
            erzeugen wir eine Referenz (links von =) auf eine Instanz (rechts von =).

"""


# Instanz

""" 
Datentyp: type()
Der Datentyp dient bei der Erzeugung der Instanz als 'Bauplan' und legt fest, 
welche Werte die Instanz annehmen darf. 
"""
a = 12345
type(a) # Datentyp
# Out[3]: int
type(123) == int
# Out[6]: True
type(123) == str
# Out[7]: False

"""
Identität: id()
Die Identität dient zur Unterscheidung von unterschiedlichen Instanzen 
desselben Datentyps.
"""

id(a)
# Out[8]: 2624709727088
b = 12345
id(b)
# Out[9]: 2624709729936