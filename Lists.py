# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:17:58 2022

@author: Luqmon
"""

#List quyidagicha yaratiladi:
    
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat

#Ro'yhat elementlari.

#print("Birinchi meva: ", mevalar[0])
#print("Ikkinchi meva: ", mevalar[1])

#Agar list ichidagi elementlar matn ko'rinishid bo'lsa, ularga string
#metodlarni qo'llashimiz mumkin:

#print("Birinchi meva: ", mevalar[0].title())
#print("Ikkinchi meva: ", mevalar[1].upper())
#print("Olma sharbati uchun", mevalar[0], "zarur")

#List elementlari ustida arifmetik amallar bajarish:

#print(narhlar[2]+narhlar[3])

narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 15000 # 1-qiymatni 15000 ga o'zgartiramiz
narhlar[1] = 12000 # 2-qiymatni 12000 ga o'zgartiramiz
narhlar[3] = narhlar[2] + 500 # 4-qiymatga 500 qo'shamiz

#print(narhlar)

#.appen() metodi

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
mevalar.append('tarvuz') #mevalarga tarvuz qo'shamiz
#print(mevalar)

#bo'sh ro'yxat

cars = [] # bo'sh ro'yxat yaratamiz
cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
#print(cars)

#insert metodi

cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
#print(cars)