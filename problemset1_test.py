import problemset1_problema1 as p1
import problemset1_problema2 as p2

# esempi problema 1
p1_istanze = ['()))((', ')(())()', '()))()(())(']
for x in p1_istanze:
    print(f"La sequenza \'{x}\' e\' {p1.bilancia(x)}-bilanciabile")

# esempi problema 2
p2_istanze = [
#   (delta, tempi di arrivo, M) 
    (4, [5,15,20,40,43,45,50], 60),
    (2, [2,10,11,15], 20),
    (5, [0,15,20,30,60], 80)
]
for x in p2_istanze:
    d1 = p2.alg_find_delta(x[0], x[1], x[2])
    print(f"d: {x[0]}, M: {x[2]}, lista: {x[1]}. delta primo = {d1}")