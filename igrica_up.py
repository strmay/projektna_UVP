#to je uporabniski vmesnik

import tkinter as tk
import random
import re
import igrica

DIM_OKNA = 1000
ST_BESED = 15
ZACETNO_BESEDILO = """Podravljeni, cilj igre je poiskati {} angleških besed,
ki se skrivajo v zgornji mreži. Mednje spada vse od blagovnih znamk, do lastnih osebnih imen.
Ko besedo najdete, z miško kliknite na zacetno polje besede, gumb drzite in sputite na polju zadnje črke besede.
Če poiščete besedo, za katero ste prepričani, da obstaja, pa je kljub temu ne prepoznam kot rešitev,
se Vam v imenu avtorja vnaprej opravičujem, saj moja datoteka besed ne vsebuje vseh, ki obstajajo.""".format(ST_BESED)

def polje_v_koordinate(n, m): #prvi kvadratek ima "fejk koordinate" (0,0)
    return 10 + 59/2 + n*59, 10 + 59/2 + m*59

def koordinate_v_polje(x):
    if 10 < x < 600:
        n, i = 0, 10
        while i+59 < x and i < 600:
            n += 1
            i += 59
        return n

koordinate = {"x":0,"y":0,"x2":0,"y2":0}

class Krizanka:
    
    def __init__(self, okno):
        self.igra = igrica.Igra()
        self.crte = []
        self.najdene = []
        self.okno = okno
        self.igralna_plosca = tk.Canvas(okno, height=DIM_OKNA, width=DIM_OKNA)
        self.igralna_plosca.pack()
        for i in range(69, 659, 59):                
            self.igralna_plosca.create_rectangle(10, 10, i, 600)
            self.igralna_plosca.create_rectangle(10, 10, 600, i)
        polja = self.igra.naredi_krizanko(ST_BESED)
        uporabljene_besede = self.igra.bes_v_krizanki()
        zacetna_polja = self.igra.zacetna()
        smeri = self.igra.smeri_bes()
        for i in polja:
            self.igralna_plosca.create_text(polje_v_koordinate(i[0], i[1])[0], polje_v_koordinate(i[0], i[1])[1], text=polja[i].upper())
        self.igralna_plosca.create_text(375, 650, text=ZACETNO_BESEDILO)
        self.igralna_plosca.bind("<Button-1>", self.pritisni_mis)
        self.igralna_plosca.bind("<ButtonRelease-1>", self.spusti_mis)

    def pritisni_mis(self, event1): 
        koordinate["x"] = polje_v_koordinate(koordinate_v_polje(event1.x),koordinate_v_polje(event1.y))[0]
        koordinate["y"] = polje_v_koordinate(koordinate_v_polje(event1.x),koordinate_v_polje(event1.y))[1]

    def spusti_mis(self, event2):
        resitev = tk.Button(self.igralna_plosca, text="Prikaži rešitev", command=self.prikazi_resitev)
        prikaz_bes = tk.Button(self.igralna_plosca, text="Prikaži besede", command=self.namigi)
        koordinate["x2"] = polje_v_koordinate(koordinate_v_polje(event2.x),koordinate_v_polje(event2.y))[0]
        koordinate["y2"] = polje_v_koordinate(koordinate_v_polje(event2.x),koordinate_v_polje(event2.y))[1]
        self.crte.append(self.narisi_crto())
        self.najdene.append(((koordinate_v_polje(koordinate["x"]), koordinate_v_polje(koordinate["y"])), (koordinate_v_polje(koordinate["x2"]), koordinate_v_polje(koordinate["y2"]))))
        if len(self.crte) == 8:
            self.igralna_plosca.create_window(800, 100, window=prikaz_bes)
        if len(self.crte) == 15:
            self.igralna_plosca.create_window(800, 50, window=resitev)
            
    def narisi_crto(self):
        self.igralna_plosca.create_line(koordinate["x"], koordinate["y"], koordinate["x2"], koordinate["y2"])

    def prikazi_resitev(self):
        for bes in self.igra.bes_v_krizanki():
            prvo_polje = self.igra.zacetna()[bes]
            zadnje_polje = self.zadnja_polja(bes)
            self.igralna_plosca.create_line(polje_v_koordinate(prvo_polje[0], prvo_polje[1])[0],polje_v_koordinate(prvo_polje[0], prvo_polje[1])[1], polje_v_koordinate(zadnje_polje[0], zadnje_polje[1])[0], polje_v_koordinate(zadnje_polje[0], zadnje_polje[1])[1], fill="red", dash=(4, 4))

    def zadnja_polja(self, bes):
        prvo_polje = self.igra.zacetna()[bes]
        if self.igra.smeri_bes()[bes] == "vd":
            zadnje_polje = (prvo_polje[0], prvo_polje[1]+len(bes)-1)
        elif self.igra.smeri_bes()[bes] == "vg":
            zadnje_polje = (prvo_polje[0], prvo_polje[1]-len(bes)+1)
        elif self.igra.smeri_bes()[bes] == "hd":
            zadnje_polje = (prvo_polje[0]+len(bes)-1, prvo_polje[1])
        elif self.igra.smeri_bes()[bes] == "hl":
            zadnje_polje = (prvo_polje[0]-len(bes)+1, prvo_polje[1])
        elif self.igra.smeri_bes()[bes] == "dd":
            zadnje_polje = (prvo_polje[0]+len(bes)-1, prvo_polje[1]+len(bes)-1)
        elif self.igra.smeri_bes()[bes] == "dg":
            zadnje_polje = (prvo_polje[0]-len(bes)+1, prvo_polje[1]-len(bes)+1)
        elif self.igra.smeri_bes()[bes] == "lg":
            zadnje_polje = (prvo_polje[0]+len(bes)-1, prvo_polje[1]-len(bes)+1)
        elif self.igra.smeri_bes()[bes] == "ld":
            zadnje_polje = (prvo_polje[0]-len(bes)+1, prvo_polje[1]+len(bes)-1)
        return zadnje_polje

    def namigi(self):
        i = 150
        for bes in self.igra.bes_v_krizanki():
            if (self.igra.zacetna()[bes], self.zadnja_polja(bes)) in self.najdene or (self.zadnja_polja(bes), self.igra.zacetna()[bes]) in self.najdene:
                self.igralna_plosca.create_text(800, i, text=bes, fill="green")
                i += 30
            else:
                self.igralna_plosca.create_text(800, i, text=bes, fill="red")
                i += 30
                
okno = tk.Tk()
program = Krizanka(okno)
okno.resizable(width=False, height=False)
okno.mainloop()

