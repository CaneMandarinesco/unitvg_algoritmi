
def find_delta(d, t, M, j):
    # d:  delta
    # t:  lista di tempi di arrivo
    # M:  tempo limite
    # j:  indice sinistro, considero l'array a da j a n
    # ritorna: delta primo, massimo, possibile per l'array da j a n

    n  = len(t)

    # -- CASO BASE --
    if n-j == 1:
        # e' l'unico delta primo possibile per un array di 1 elemento
        d1 = M - t[n-1] - 1
        if d1 < d:
            return -1
        return d1

    # -- CASO RICORSIVO --
    d1 = find_delta(d, t, M, j+1)

    # controlla se si crea una coda.
    if t[j] + d1 > t[j+1]:
        # devo aggiornare d1 altrimenti sforo sicuramente il tempo M.
        d1 = (M - t[j] - 1) // (n-j)
        if d1 < d:
            return -1
    
    return d1
    

def alg_find_delta(d, t, M):
    # metodo wrapper per find_delta
    return find_delta(d, t, M, 0)