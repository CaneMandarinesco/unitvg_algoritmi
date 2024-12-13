def start(s):
    return s[0]

def end(s):
    return s[1]

def lens(s):
    return (s[1] - s[0]) + 1

def value(s):
    return s[2]

def calcola_max_score(S,n,k):
    X = S
    S.sort(key= lambda s: value(s), reverse=True)
    
    occup = (0,0)
    empty = (0,0)
    for i in range(0,n,2):
        score = 0
        # proprieta: value(s1) >= value(s2) 
        s1, s2 = (S[i], S[i+1])

        # Trova quante monete si sovrapp

        # Calcola il massimo per la coppia di sequenze
        score += lens(s1) * value(s1)
        # s1 contiene s2
        if start(s2) >= start(s1) and end(s2) <= end(s1):
            pass
        # s2 contiene s1
        elif start(s1) >= start(s2) and end(s1) <= end(s2):
            score += (start(s1) - start(s2)) * value(s2)
            score += (end(s2) - end(s1)) * value(s2)
        # s1 supera s2
        elif start(s2) <= end(s1) <= end(s2) and end(s2) > end(s1):
            score += (start(s1) - start(s2)) * value(s2)
        # s2 supera s1
        elif start(s1) <= end(s2) <= end(s1) and end(s1) > end(s2):
            score += (end(s2) - end(s1)) * value(s2)
        # s1 e s2 consecutivi o ci sono spazi vuoti tra loro
        else:
            score += lens(s2) * value(s2)

            # s1 subito dopo/prima s2?
            if end(s1)+1 == start(s2) or end(s2)+1 == start(s1):
                empty = (0,0)
            elif end(s1)+1 <= start(s2)-1:
                empty = (end(s1)+1, start(s2)-1)
            elif end(s2)+1 <= start(s1)-1:
                empty = (end(s2)+1, start(s1)-1)

        print(s1,s2, score, empty)

S = [(2,7,4,1), (3,3,9,3), (6,9,2,2), (7,8,5,3), (10,10,5,1), (10,10,1,3)]
n = 6
k = 3
#calcola_max_score(S,n,k)

S = [(1,3,2,1), (1,3,9,3), (3,5,10,2), (7,11,6,3), (9,9,9,2), (13,14,3,1)]
n = 6
k = 3
calcola_max_score(S,n,k)