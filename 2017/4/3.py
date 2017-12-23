#!/usr/bin/python3
# note to self: ovo rjesit u c-u je  nepotrebno
# komplicirano, python gets the job done

N=int(input())
M=int(input())
K=int(input())

lampe=[0 for i in range(N+1)]
rupe = []
nove_lampe = 0

for i in range(M):
    indeks = int(input())
    lampe[indeks] = 1

    for j in range(K+1):
        if indeks-j >= 0:
            lampe[indeks-j]=1
        if indeks+j <= N:
            lampe[indeks+j]=1


u_rupi=False
duljina_trenutne_rupe=int()

for i in range(N+1):
    if lampe[i]==0:
        if u_rupi==True:
            duljina_trenutne_rupe += 1
        else:
            u_rupi=True
            duljina_trenutne_rupe = 1
    else:
        if u_rupi==True:
            # upravo smo izisli iz rupe
            rupe.append(duljina_trenutne_rupe)
        u_rupi=False

# ako smo zavrsili s rupom, treba ju zbrojit, jer to inace radimo
# tek kada izadjemo iz rupe (a tu nismo jer je jos rupa na kraju :))
if u_rupi==True:
    rupe.append(duljina_trenutne_rupe)


# izracunaj broj semafora koje treba stavit.
# ispada da samo treba podijelit (i zaokruzit na veci broj ako je potrebno) velicinu
# mracne rupe sa 2*K+1 (na papiru se da izvest, quick maths)
for rupa in rupe:
    rez = rupa // (2*K+1)
    if rupa%(2*K+1) != 0:
        rez+=1
    nove_lampe += rez

print(nove_lampe)
