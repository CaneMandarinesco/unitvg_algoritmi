import problemset1_problema1 as p1
import problemset1_problema2 as p2

# esempi problema 1
p1_istanze = ['()))((', ')(())()', '()))()(())(']
for x in p1_istanze:
    print(f"La sequenza \'{x}\' e\' {p1.bilancia(x)}-bilanciabile")

# esempi problema 2
p2_istanze = [
#   (delta, tempi di arrivo,    M) 
    (4,     [5,15,20,40,43,45,50], 60),
    (2,     [2,10,11,15],          20),
    (10,    [2,10,11,15],          40), # invalid
    (12,    [2,10,11,15],          10), # invalid
    (5,     [2,10,11,15,30,31,32], 50),
    (10,    [1,2,3,4,5,60],        73),
    (3,     [0,1,2,10,15],         30),
    (2,     [0,1,2,10,15,20],      100),
    (5,     [2,10,11,15,30,31,45], 50),
    (12,    [1,2,3,4,10,60],       73),
    (3,     [0,1,2,10,15],         200),
    (10,    [0,1,2,10,15,20],      150)

]
for x in p2_istanze:
    d1 = p2.alg_find_delta(x[0], x[1], x[2])
    print(f"d: {x[0]}, M: {x[2]}, lista: {x[1]}. delta primo = {d1}")
    if d1 == -1:
        print("\x1b[31minvalid input\x1b[0m")
        continue
    time = p2.test_delta(d1, x[1], x[2])
    error = p2.test_delta(d1+1, x[1], x[2]) < x[2]
    print(f"test time: {time}. ", "\x1b[31merror\x1b[0m" if error else "\x1b[32mok\x1b[0m")