#!/usr/bin/python3

# TODO (stjepanbrkicc)
# * refactor this crap to make it readable


N = int() # broj zupanija
M = int() # broj kandidiranih predsjednika
K = int() # kandidat koji Zdravka zanima

l = input().split(" ")
N = int(l[0])
M = int(l[1])
K = int(l[2])

preference = [ list() for i in range(0,N+1)]
odustali = []

for i in range(1,N+1):
    pref = input().split(" ")
    for x in pref:
        preference[i].append(int(x))

# 1 podzadatak

stanje = {}
max = None
def proracunaj_stanje():
    stanje = {}
    for i in range(1,N+1):
        for t in range(M):
            if preference[i][t] not in odustali:
                preferenca = preference[i][t]
                if preferenca not in stanje.keys():
                    stanje[preferenca] = 1
                else:
                    stanje[preferenca] += 1

                break

    max = None
    for kandidat in stanje.keys():
        if max == None:
            max = kandidat

        if stanje[kandidat] > stanje[max] and kandidat < max:
            max = kandidat

    return max, stanje

max, stanje = proracunaj_stanje()
print(max)


# 2 podzatadak
kandidati_sortirani = list(stanje)
kandidati_sortirani.sort(key=lambda x: stanje[x], reverse=True)

pobjednik, stanje = proracunaj_stanje()

brojac = 0
while pobjednik!=K:
    odustali.append(kandidati_sortirani[0])
    brojac+=1
    pobjednik, stanje = proracunaj_stanje()
    if pobjednik == K:
        break
    kandidati_sortirani = list(stanje)
    kandidati_sortirani.sort(key=lambda x: stanje[x], reverse=True)



print(brojac)



