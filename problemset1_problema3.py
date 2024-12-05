import math

# ogni nodo contiene:
# * inizio
# * fine
# * numero_cfu
# * indice di s1
# * indice di s2

def figlioDestro(i, n):
    if (i*2) + 1 <= n:
        return (i*2) + 1
    return -1

def figlioSinistro(i, n):
    if (i*2) <= n:
        return (i*2)
    return -1

def max_cfu(s1, s2):
    s1_s, s1_t, s1_v, s1_k = s1
    s2_s, s2_t, s2_v, s2_k = s2

    s1_len = s1_t - s1_s + 1
    s2_len = s2_t - s2_s + 1

    # se le sequenze sono su corsie diverse
    if (s1_k != s2_k):
        # se s1 e s2 non si sovrappongono... easy!
        if s1_t < s2_s:
            return (s1_s, s2_t, (s1_len*s1_v) + (s2_len)*s2_v, 0, 0)

        # se s1 e s2 si sovrappongono...
        # se s1 contiene s2
        if s1_t >= s2_t:
            # se i cfu in s1 valgono piu di s2
            if s1_v >= s2_v:
                return (s1_s, s1_t, s1_len*s1_v, 0, 0)
            # se i cfu in s1 valgono di meno
            return (s1_s, s1_t, ((s1_len-s2_len)*s1_v) + (s2_len * s2_v), 0, 0)
        
        # se una parte di s2 si trova in s1 e l'altra e' fuori...
        # se i cfu in s1 valgono piu di s2
        if s1_v >= s2_v:
            return (s1_s, s2_t, (s1_len * s_v) + ((s2_t - s1_t) * s2_v), 0, 0)
        
        # se i cfu in s1 valgono meno di s2
        return (s1_s, s2_t, ((s2_s - s1_s) * s1_v) + (s2_len*s2_v), 0, 0)
    
    # se sono sulla stessa corsia, non si sovrappongono
    return (s1_s, s_end, (s1_len*s1_v)+(s2_len*s2_v), 0, 0)

def unisici_soluzioni(T, S, i, n, k):
    sx = figlioSinistro(i, n)
    dx = figlioDestro(i, n)

    print(f"nodo {i}, devo unire le soluzioni: {T[sx]} e {T[dx]}")

    if sx == -1 or dx == -1:
        print('diocane errore!')
    
    return ()


# variabile globale per tenere conto della sequenza corrente
j = 0
# variabile globale per tenere il numero di nodi
nodi = 0
def calcola_cfu(T, S, i, n, k):
    global j, nodi
    # T: albero binario
    # S: sequenza in input
    # i: indice del nodo per cui devo calcolare i cfu
    # n: numero di sequenze
    # k: corsie

    sx = figlioSinistro(i, nodi)
    dx = figlioDestro(i, nodi)

    if (dx == -1 and sx == -1):
        # -- CASO BASE --

        if(j+1 < n):
            # lavoro su due sequenze
            T[i] = max_cfu(S[j], S[j+1])
            T[i][3] = j
            T[i][4] = j+1
        else:
            # lavoro su una sola sequenza
            s = S[j]
            #      (start, fine, valore, s1, s2)
            T[i] = (s[0], s[1], (s[1]-s[0] + 1) * s[2], j, -1)

        j += 2
    else:
        # -- CASO RICORSIVO --
        T = calcola_cfu(T, S, sx, n, k)
        T = calcola_cfu(T, S, dx, n, k)

        # metti insieme le soluzioni
        s = unisici_soluzioni(T, S, i, n, k)

    return T

def algoritmo(S, n, k):
    # resetta sempre la variabile globale!
    global j, nodi
    j = 0

    # T di grandezza n+1. la radice si trova in posizione 1
    # T[i] = (inizio, fine, cfu)

    # O(n)
    T = []
    nodi = n-1 if n%2 == 0 else n
    for i in range(0,nodi+1):
        T.append((0,0,0))

    T = calcola_cfu(T, S, 1, n, k)

    print(T)

    return T[1]

# S[i] = (s: start, t: fine, v: valore, k: corsia)
S = [(2,7,4,1), (3,3,9,3), (6,9,2,2), (7,8,5,3), (10,10,5,1), (10,10,1,3)]
n = len(S)
k = 3
algoritmo(S,n,k)