import math
import random

jml_populasi = 10 #ukuran populasi
count_generasi = 50 #generasi sebanyak 50 kali

def fx(x1,x2):
    if x2 == 0:
        return math.cos(x1) * math.sin(x2) - x1/1
    else:
        return math.cos(x1) * math.sin(x2) - x1/(x2**2)+1


def get_populasi(count):#mendapatkan x1 x2 kromosom
    populasi = []
    for i in range(count):
        kromosom = {
          "x1": random.uniform(-1, 2),
          "x2": random.uniform(-1, 1)
        }
        populasi.append(kromosom)
    return populasi

def minimasi_fitness(populasi):#cari nilai minimal fitness
    hasil = []
    a = 3
    for i in range(jml_populasi):
        c = populasi[i]
        h = fx(c['x1'], c['x2'])
        fit = 1 / (h + a)
        hasil.append({'idx': i,'h': h,'fit': fit})
    return hasil

def seleksi_ortu(populasi, fitness_results):#tournament selection
    sort_fitness = sorted(fitness_results, key=lambda x: x['fit'], reverse=True) 
    ortu1 = populasi[sort_fitness[0]['idx']]
    ortu2 = populasi[sort_fitness[1]['idx']]
    return ortu1, ortu2

def crossover(parent):#crossover secara uniform
    prt1, prt2 = parent
    i = random.uniform(0, 1)
    if i < 0.5:
        return {
          'x1': prt1['x1'],'x2': prt2['x2']}
    else:
        return {'x1': prt2['x1'], 'x2': prt1['x2']}

def mutasi(childs):#mutasi bersifat 50:50
    i = random.randint(0, 1)
    if i == 1:
        return {'x1': childs['x1'],'x2': random.uniform(-1, 1)}
    else:
        return {'x1': random.uniform(-1, 2),'x2': childs['x2']}

def survivors(populasi, fitness_results, childs):#steady state
    sort_fitness = sorted(fitness_results, key=lambda x: x['fit'], reverse=True)
    death_idx = sort_fitness[len(sort_fitness)-1]['idx']
    populasi[death_idx] = childs
    return populasi

#Algoritma GA
populasi = get_populasi(jml_populasi)
for i in range(count_generasi):
    fitness_results = minimasi_fitness(populasi)
    parent = seleksi_ortu(populasi, fitness_results)
    childs = crossover(parent)
    childs = mutasi(childs)
    populasi = survivors(populasi, fitness_results, childs)

print(" value x1 dan x2")
for p in populasi:
    print('\n',p)
print('\n',"value pada array fitness")
for s in fitness_results:
    print('\n',s)

#incomplete