# -*- coding: utf-8 -*-
"""1.Homework.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14H_PfYybKJRWRUexsEWW2kw82fxl_MaI
"""
a = float(input("Введите число согласно условия: "))
b = float(input("Введите число согласно условия: "))
V_cuba = a**3
S_cuba = 6*a**2
M_arif = (a + b)/2
M_geom = (a * b)**0.5
C_gipo = (a**2 + b**2)**0.5
S_treu = (a * b)/2
print('Объём куба равен ' + str(V_cuba))
print('Площадь куба равна ' + str(S_cuba))
print('Среднеарифметическое равно ' + str(M_arif))
print('Среднегеометрическое равно ' + str(M_geom))
print('Гипотенуза равна ' + str(C_gipo))
print('Площадь треугольника равна ' + str(S_treu))