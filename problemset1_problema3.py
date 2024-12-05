
# variabili globali
nodi = 0
T = []
j = 0

def figlioSx(i):
    if (i*2) <= nodi:
        return (i*2)
    return -1

def figlioDx(i):
    if (i*2) + 1 <= nodi:
        return (i*2) + 1
    return -1

def unisci_soluzioni(S, i, n, k):
    # TODO: ora pero' devo iterare su altre liste...
    s1_s, s1_t, s1_v, s1_k, _ = s1 = T[figlioSx(i)]
    s2_s, s2_t, s2_v, s2_k, _ = s2 = T[figlioDx(i)]

    if s1_k != s2_k:
        # s2 compreso in s1?
        if s1_t > s2_t:
            if s1_v > s2_v:
                return s1
            
            return  (s1_s,   s2_s-1, s1_v, s1_k, 
                    (s2_s,   s2_t,   s2_v, s2_k, 
                    (s2_t+1, s1_t,   s1_v, s1_k, None)))
        # s2 e s1 terminano nello stesso t?
        if s1_t == s2_t:
            if s1_v > s2_v:
                return s1
            
            return  (s1_s, s2_s-1, s1_v, s1_k, 
                    (s2_s, s2_t,   s2_v, s2_k, None))
        
        # s2 termina dopo s1?
        if s1_t < s2_t:
            if s1_v > s2_v:
                return  (s1_s, s1_t, s1_v, s1_k,
                        (s1_t+1, s2_t, s2_v, s2_k, None))
            return  (s1_s, s2_s-1, s1_v, s1_k, 
                    (s2_s, s2_t,   s2_v, s2_k, None))

def tree_calcola_max_score(S,i,n,k):
    """_summary_
    Calcola il massimo score ottenibile in una sequenza S sfruttando 
    la struttura dati ad albero binario contenuta in T
    Args:
        S (List): sequenze di monete
        i (int): nodo da usare come radice
        n (int): numero di sequenze
        k (int): numero di corsie
    """
    global T, nodi, j

    sx = figlioSx(i)
    dx = figlioDx(i)

    if dx == sx == -1:
        # -- CASO BASE --
        T[i] = (*S[j], None)
        j+=1

    else:
        # -- CASO RICORSIVO --
        tree_calcola_max_score(S, sx, n ,k)
        tree_calcola_max_score(S, dx, n, k)

        # metti insieme le soluzioni
        T[i] = unisci_soluzioni(S, i, n, k)

def alg_calcola_max_score(S,n,k):
    """_summary_
    Calcola il massimo score ottenibile in una sequenza S
    Args:
        S (List): sequenze di monete
        n (int): numero di sequenze
        k (int): numero di corsie
    """
    global T, nodi, v
    nodi = (2*n)-1
    v = 0
    T = [(0,0,0,0,None) for _ in range(0,nodi+1)]

    tree_calcola_max_score(S,1,n,k)
    print(T)

S = [(2,7,4,1), (3,3,9,3), (6,9,2,2), (7,8,5,3), (10,10,5,1), (10,10,1,3)]
n = len(S)
k = 3
alg_calcola_max_score(S,n,k)