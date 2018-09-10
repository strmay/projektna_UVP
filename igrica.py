#zaenkrat je to samo file

import tkinter as tk
import random
import re
    
uporabljene_besede = [] #to bo seznam uporabljenih besed
polja = {} #to bo slovar polj in pripadajočih črk
zacetna_polja = {} #to bo slovar besed in pripadajocih zacetnih polj
smeri = {} #to bo slovar besed in pripadajocih smeri

ang_abeceda = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

vsa_polja = [(i, j) for i in range(0, 10) for j in range(0, 10)]

with open("words.txt") as f:        #tu odprem dokument z besedami, ki lahko nastopijo v igrici
    
    besede = f.read().splitlines()
    besede = [i[:-1] for i in besede] #zato, kr na macu doda kr se dve posevnici nakoncu
    besede = [i for i in besede if len(i) > 3 and len(i) <= 10]

    class Igra:
    
        def postavitev_naslednje_besede(self):
            while True:
                zacetno_naslednje = random.choice(vsa_polja)
                mozne_smeri = ["vd", "vg", "hd", "hl", "dd", "dg", "lg", "ld"]  #vd-vertikalno dol, vg-vertikalno gor, hd-horizontalno desno, hl-horizontalno levo, dd-diagonalno dol, dg-diagonalano gor
                while mozne_smeri != []:
                    smer = random.choice(mozne_smeri)
                    if smer == "vd":
                        mozne_besede = [bes for bes in besede if len(bes) <= 9 - zacetno_naslednje[1]]
                        for i in range(zacetno_naslednje[1], 10):
                            if (zacetno_naslednje[0], i) in list(polja.keys()):
                                mozne_besede = [bes for bes in mozne_besede if (re.search(r"."*(i-zacetno_naslednje[1]) + "{}.*".format(polja[(zacetno_naslednje[0], i)]), bes) and bes == re.search(r"."*(i-zacetno_naslednje[1]) + "{}.*".format(polja[(zacetno_naslednje[0], i)]), bes).group()) or len(bes) <= i-zacetno_naslednje[1]] 
                        if mozne_besede != []:
                            naslednja_beseda = random.choice(mozne_besede)
                            uporabljene_besede.append(naslednja_beseda)
                            smeri[naslednja_beseda] = smer
                            zacetna_polja[naslednja_beseda] = zacetno_naslednje
                            for j in range(zacetno_naslednje[1], zacetno_naslednje[1]+len(naslednja_beseda)):
                                if (zacetno_naslednje[0], j) not in list(polja.keys()):
                                    polja[(zacetno_naslednje[0], j)] = naslednja_beseda[j-zacetno_naslednje[1]]
                                else:
                                    pass
                            del besede[besede.index(naslednja_beseda)]
                            return zacetna_polja
                            return smeri
                            return polja
                            return uporabljene_besede
                        else:
                            del mozne_smeri[mozne_smeri.index("vd")]
                                                      
                    elif smer == "vg":
                        mozne_besede = [bes for bes in besede if len(bes) <= zacetno_naslednje[1]]
                        for i in range(0, zacetno_naslednje[1]+1):
                            if (zacetno_naslednje[0], i) in list(polja.keys()):
                                mozne_besede = [bes for bes in mozne_besede if (re.search(r"."*(zacetno_naslednje[1]-i) + "{}.*".format(polja[(zacetno_naslednje[0], i)]), bes) and bes == re.search(r"."*(zacetno_naslednje[1]-i) + "{}.*".format(polja[(zacetno_naslednje[0], i)]), bes).group()) or len(bes) <= zacetno_naslednje[1]-i]
                        if mozne_besede != []:
                            naslednja_beseda = random.choice(mozne_besede)
                            uporabljene_besede.append(naslednja_beseda)
                            smeri[naslednja_beseda] = smer
                            zacetna_polja[naslednja_beseda] = zacetno_naslednje
                            for j in range(zacetno_naslednje[1]+1- len(naslednja_beseda), zacetno_naslednje[1]+1):
                                if (zacetno_naslednje[0], j) not in list(polja.keys()):
                                    polja[(zacetno_naslednje[0], j)] = naslednja_beseda[zacetno_naslednje[1]-j]
                                else:
                                    pass
                            del besede[besede.index(naslednja_beseda)]
                            return zacetna_polja
                            return smeri
                            return polja
                            return uporabljene_besede
                        else:
                            del mozne_smeri[mozne_smeri.index("vg")]
                        
                    elif smer == "hd":
                        mozne_besede = [bes for bes in besede if len(bes) <= 9 - zacetno_naslednje[0]]
                        for i in range(zacetno_naslednje[0], 10):
                            if (i, zacetno_naslednje[1]) in list(polja.keys()):
                                mozne_besede = [bes for bes in mozne_besede if (re.search(r"."*(i-zacetno_naslednje[0]) + "{}.*".format(polja[(i, zacetno_naslednje[1])]), bes) and bes == re.search(r"."*(i-zacetno_naslednje[0]) + "{}.*".format(polja[(i, zacetno_naslednje[1])]), bes).group()) or len(bes) <= i-zacetno_naslednje[0]]
                        if mozne_besede != []:
                            naslednja_beseda = random.choice(mozne_besede)
                            uporabljene_besede.append(naslednja_beseda)
                            smeri[naslednja_beseda] = smer
                            zacetna_polja[naslednja_beseda] = zacetno_naslednje
                            for j in range(zacetno_naslednje[0], zacetno_naslednje[0]+len(naslednja_beseda)):
                                if (j, zacetno_naslednje[1]) not in list(polja.keys()):
                                    polja[(j, zacetno_naslednje[1])] = naslednja_beseda[j-zacetno_naslednje[0]]
                                else:
                                    pass
                            del besede[besede.index(naslednja_beseda)]
                            return zacetna_polja
                            return smeri
                            return polja
                            return uporabljene_besede
                        else:
                            del mozne_smeri[mozne_smeri.index("hd")]
                    
                    elif smer == "hl":
                        mozne_besede = [bes for bes in besede if len(bes) <= zacetno_naslednje[0]]
                        for i in range(0, zacetno_naslednje[0]+1):
                            if (i, zacetno_naslednje[1]) in list(polja.keys()):
                                mozne_besede = [bes for bes in mozne_besede if (re.search(r"."*(zacetno_naslednje[0]-i) + "{}.*".format(polja[(i, zacetno_naslednje[1])]), bes) and bes == re.search(r"."*(zacetno_naslednje[0]-i) + "{}.*".format(polja[(i, zacetno_naslednje[1])]), bes).group()) or len(bes) <= zacetno_naslednje[0]-i]
                        if mozne_besede != []:
                            naslednja_beseda = random.choice(mozne_besede)
                            uporabljene_besede.append(naslednja_beseda)
                            smeri[naslednja_beseda] = smer
                            zacetna_polja[naslednja_beseda] = zacetno_naslednje
                            for j in range(zacetno_naslednje[0]+1-len(naslednja_beseda), zacetno_naslednje[0]+1):
                                if (j, zacetno_naslednje[1]) not in list(polja.keys()):
                                    polja[(j, zacetno_naslednje[1])] = naslednja_beseda[zacetno_naslednje[0]-j]
                                else:
                                    pass
                            del besede[besede.index(naslednja_beseda)]
                            return zacetna_polja
                            return smeri
                            return polja
                            return uporabljene_besede
                        else:
                            del mozne_smeri[mozne_smeri.index("hl")]
    
                    elif smer == "dd":
                        mozne_besede = [bes for bes in besede if len(bes) <= 9 - max(zacetno_naslednje[0], zacetno_naslednje[1])]
                        for i in range(0, 10 - max(zacetno_naslednje[0], zacetno_naslednje[1])):
                            if (zacetno_naslednje[0]+i, zacetno_naslednje[1]+i) in list(polja.keys()):
                                mozne_besede = [bes for bes in mozne_besede if (re.search(r"."*i + "{}.*".format(polja[(zacetno_naslednje[0]+i, zacetno_naslednje[1]+i)]), bes) and bes == re.search(r"."*i + "{}.*".format(polja[(zacetno_naslednje[0]+i, zacetno_naslednje[1]+i)]), bes).group()) or len(bes) <= i]
                        if mozne_besede != []:
                            naslednja_beseda = random.choice(mozne_besede)
                            uporabljene_besede.append(naslednja_beseda)
                            smeri[naslednja_beseda] = smer
                            zacetna_polja[naslednja_beseda] = zacetno_naslednje
                            for j in range(0, len(naslednja_beseda)):
                                if (zacetno_naslednje[0]+j, zacetno_naslednje[1]+j) not in list(polja.keys()):
                                    polja[(zacetno_naslednje[0]+j, zacetno_naslednje[1]+j)] = naslednja_beseda[j]
                                else:
                                    pass
                            del besede[besede.index(naslednja_beseda)]
                            return zacetna_polja
                            return smeri
                            return polja
                            return uporabljene_besede
                        else:
                            del mozne_smeri[mozne_smeri.index("dd")]
    
                    elif smer == "dg":
                        mozne_besede = [bes for bes in besede if len(bes) <= min(zacetno_naslednje[0], zacetno_naslednje[1])]
                        for i in range(0, min(zacetno_naslednje[0], zacetno_naslednje[1])+1):
                            if (zacetno_naslednje[0]-i, zacetno_naslednje[1]-i) in list(polja.keys()):
                                mozne_besede = [bes for bes in mozne_besede if (re.search(r"."*i + "{}.*".format(polja[(zacetno_naslednje[0]-i, zacetno_naslednje[1]-i)]), bes) and bes == re.search(r"."*i + "{}.*".format(polja[(zacetno_naslednje[0]-i, zacetno_naslednje[1]-i)]), bes).group()) or len(bes) <= i]
                        if mozne_besede != []:
                            naslednja_beseda = random.choice(mozne_besede)
                            uporabljene_besede.append(naslednja_beseda)
                            smeri[naslednja_beseda] = smer
                            zacetna_polja[naslednja_beseda] = zacetno_naslednje
                            for j in range(0, len(naslednja_beseda)):
                                if (zacetno_naslednje[0]-j, zacetno_naslednje[1]-j) not in list(polja.keys()):
                                    polja[(zacetno_naslednje[0]-j, zacetno_naslednje[1]-j)] = naslednja_beseda[j]
                                else:
                                    pass
                            del besede[besede.index(naslednja_beseda)]
                            return zacetna_polja
                            return smeri
                            return polja
                            return uporabljene_besede
                        else:
                            del mozne_smeri[mozne_smeri.index("dg")]

                    elif smer == "lg":
                        mozne_besede = [bes for bes in besede if len(bes) <= min(9 - zacetno_naslednje[0], zacetno_naslednje[1])]
                        for i in range(0, min(9 - zacetno_naslednje[0], zacetno_naslednje[1])+1):
                            if (zacetno_naslednje[0]+i, zacetno_naslednje[1]-i) in list(polja.keys()):
                                mozne_besede = [bes for bes in mozne_besede if (re.search(r"."*i + "{}.*".format(polja[(zacetno_naslednje[0]+i, zacetno_naslednje[1]-i)]), bes) and bes == re.search(r"."*i + "{}.*".format(polja[(zacetno_naslednje[0]+i, zacetno_naslednje[1]-i)]), bes).group()) or len(bes) <= i]
                        if mozne_besede != []:
                            naslednja_beseda = random.choice(mozne_besede)
                            uporabljene_besede.append(naslednja_beseda)
                            smeri[naslednja_beseda] = smer
                            zacetna_polja[naslednja_beseda] = zacetno_naslednje
                            for j in range(0, len(naslednja_beseda)):
                                if (zacetno_naslednje[0]+j, zacetno_naslednje[1]-j) not in list(polja.keys()):
                                    polja[(zacetno_naslednje[0]+j, zacetno_naslednje[1]-j)] = naslednja_beseda[j]
                                else:
                                    pass
                            del besede[besede.index(naslednja_beseda)]
                            return zacetna_polja
                            return smeri
                            return polja
                            return uporabljene_besede
                        else:
                            del mozne_smeri[mozne_smeri.index("lg")]

                    elif smer == "ld":
                        mozne_besede = [bes for bes in besede if len(bes) <= min(9 - zacetno_naslednje[1], zacetno_naslednje[0])]
                        for i in range(0, min(9 - zacetno_naslednje[1], zacetno_naslednje[0])+1):
                            if (zacetno_naslednje[0]-i, zacetno_naslednje[1]+i) in list(polja.keys()):
                                mozne_besede = [bes for bes in mozne_besede if (re.search(r"."*i + "{}.*".format(polja[(zacetno_naslednje[0]-i, zacetno_naslednje[1]+i)]), bes) and bes == re.search(r"."*i + "{}.*".format(polja[(zacetno_naslednje[0]-i, zacetno_naslednje[1]+i)]), bes).group()) or len(bes) <= i]
                        if mozne_besede != []:
                            naslednja_beseda = random.choice(mozne_besede)
                            uporabljene_besede.append(naslednja_beseda)
                            smeri[naslednja_beseda] = smer
                            zacetna_polja[naslednja_beseda] = zacetno_naslednje
                            for j in range(0, len(naslednja_beseda)):
                                if (zacetno_naslednje[0]-j, zacetno_naslednje[1]+j) not in list(polja.keys()):
                                    polja[(zacetno_naslednje[0]-j, zacetno_naslednje[1]+j)] = naslednja_beseda[j]
                                else:
                                    pass
                            del besede[besede.index(naslednja_beseda)]
                            return zacetna_polja
                            return smeri
                            return polja
                            return uporabljene_besede
                        else:
                            del mozne_smeri[mozne_smeri.index("ld")]
                            
                del vsa_polja[vsa_polja.index(zacetno_naslednje)]

        def naredi_krizanko(self, n):
            for i in range(1, n+1):
               self.postavitev_naslednje_besede()
            for polje in vsa_polja:
                x, y = polje
                if polje not in list(polja.keys()):
                    polja[(x, y)] = random.choice(ang_abeceda)
                else:
                    pass
            return polja

        def bes_v_krizanki(self):
            return uporabljene_besede

        def zacetna(self):
            return zacetna_polja

        def smeri_bes(self):
            return smeri

igra = Igra()
