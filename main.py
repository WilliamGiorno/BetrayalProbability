def funzione_iniziale(facce, somma_cercata):   
    
    combinazione_totali = []
    for a in facce:
        for b in facce:
            for c in facce:
                for d in facce:
                    for e in facce:
                        for f in facce:
                            for g in facce:
                                for h in facce:
                                    combinazione_totali.append(a+b+c+d+e+f+g+h)
    combinazioni_giuste = 0
    for t in combinazione_totali:
        if t >= somma_cercata:
            combinazioni_giuste += 1
    return combinazioni_giuste


def conta_combinazioni(dadi_rimanenti, somma_rimanente, memo):
    # Caso base: nessun dado rimanente
    if dadi_rimanenti == 0:
        return 1 if somma_rimanente == 0 else 0
    
    # Controlla se il risultato è già stato calcolato
    if (dadi_rimanenti, somma_rimanente) in memo:
        return memo[(dadi_rimanenti, somma_rimanente)]
    
    # Calcola il numero di combinazioni
    combinazioni = 0
    for faccia in [0, 1, 2]: 
        if somma_rimanente >= faccia:
            # Moltiplica per 2 per contare entrambe le facce identiche
            combinazioni += 2 * conta_combinazioni(dadi_rimanenti - 1, somma_rimanente - faccia, memo)
    
    # Memorizza il risultato nel dizionario
    memo[(dadi_rimanenti, somma_rimanente)] = combinazioni
    
    return combinazioni



facce = [0, 0, 1, 1, 2, 2]
numero_lanci = 8
somma_cercata = 9
combinazioni_totali = 6**numero_lanci


import cProfile
import time

start_time = time.time()
cProfile.run('funzione_iniziale(facce, somma_cercata)')
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tempo di esecuzione di funzione_precedente: {elapsed_time} secondi")

start_time = time.time()
cProfile.run('conta_combinazioni(numero_lanci, somma_cercata, {})')
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tempo di esecuzione di conta_combinazioni: {elapsed_time} secondi")