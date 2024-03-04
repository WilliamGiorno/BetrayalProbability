# Si vuole capire qual è la probabilità che lanciati 8 dadi le cui facce possibili sono 0,1,2 e ognuna ha 1/6 di possibilità di uscire, la somma dei valori ottenuti sia 9.

numero_lanci = 8
somma_cercata = 9
facce = 3

# Calcolo il numero di combinazioni possibili che mi forniscano la probabilità cercata
combinazioni = 0
for i in range(0, numero_lanci+1):
    for j in range(0, numero_lanci+1):
        for k in range(0, numero_lanci+1):
            if i+j+k == somma_cercata:
                combinazioni += 1

print("Combinazioni possibili: ", combinazioni)
print("Probabilità: ", combinazioni/(facce**numero_lanci)*100)