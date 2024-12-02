
def bilancia(S):
    n = len(S)

    h, k = 0, 0
    for c in S:
        if c == '(':
            h += 1

        # se trovo parentesi chiuse ho due casi
        else:
            # se ho incontrato in precedenza parentesi aperte
            # allora posso chiuderle
            if h > 0:
                h-=1
            # altrimenti incremento il numero di parentesi chiuse da aprire
            else:
                k+=1
    
    # una sequenza e' bilanciabile se e solo so ho stesso numero di 
    # parentesi aperte (da chiudere) e chiuse (da aprire) 
    if h == k:
        return h
    
    return float('inf')