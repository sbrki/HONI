dani = ["ponedjeljak","utorak","srijeda","cetvrtak","petak", "subota", "nedjelja"] # lista dana (moze se rjesiti i enumeracijama)
kazaljka = 0 #  pokazuje na neki dan (index) u listi dani


brojac = 22 # dan u mjesecu. Znamo da je
            # thanksgiving  u 4 tjednu sigurno
            # pa pocinjemo odbrojavati tek od 22

dan = input()
kazaljka = dani.index(dan) # nadji pocetnu kazaljku za dani dan

while(1):
    if kazaljka == 3: # Provjeravamo ako je cetvrtak
        print(brojac) # ako je to je to, printaj i
        break         # zavrsi program
    else:
        brojac +=     # ako nije, povecaj brojac dana za 1
        kazaljka = (kazaljka + 1) % len(dani) # i zarotiraj kazaljku za 1 mjesto udesno

