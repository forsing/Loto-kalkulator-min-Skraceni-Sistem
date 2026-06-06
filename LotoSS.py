# ver 2.070626
# Hypergeometric distribution h(n1,k1,n2,k2)

import math

def factorial(k2):
    if k2 == 0:
        return 1
    else:
        return k2 * factorial(k2 - 1)


def rb_round(x):
    # sve vrednosti pozitivne pa je floor(x + 0.5) dovoljno verno.
    return math.floor(x + 0.5)


print()
print()
print()
print()
print()
print('_______LOTO skraceni sistemi_______')
print()
print('LotoSS.py              ver 1.130812')
print()
print('minimalni broj kombinacija skracenog sistema')
print('i punog sistema')
print('za bilo koju igru LOTO')
print('za bilo koju garanciju')
print()
print('Hypergeometric distribution   h(n1,k1,n2,k2)')
print()


print()
print('UKUPNO BROJEVA:				n1 = ')
ukupnon1 = input().strip()
n1 = int(ukupnon1)

print('BROJEVA U KOMBINACIJI (k1<=n1):	k1 = ')
izvlacenok1 = input().strip()
k1 = int(izvlacenok1)

print('POGODJENIH BROJEVA (n2<=k1):		n2 = ')
izvucenon2 = input().strip()
n2 = int(izvucenon2)

print('GARANCIJA OD POGODJENIH (k2<=n2):	k2 = ')
pogodjenok2 = input().strip()
k2 = int(pogodjenok2)


ck1k2 = factorial(k1) // (factorial(k2) * factorial(k1 - k2))

cn1k1n2k2 = factorial(n1 - k1) // (factorial(n2 - k2) * factorial((n1 - k1) - (n2 - k2)))

cn1n2 = factorial(n1) // (factorial(n2) * factorial(n1 - n2))


h = (ck1k2 * cn1k1n2k2) / float(cn1n2)
h6 = rb_round(h * 1000000) / 1000000.0


p = 100 * h
p4 = rb_round(p * 10000) / 10000.0


kss = 1 / h
kss2 = rb_round(kss * 100) / 100.0


print()
print('h = ' + str(h6))
print()
print('verovatnoca:   ' + str(p4) + ' % ')
print()
print('minimalni broj kombinacija skracenog sistema:   ' + str(kss2))
print()
print()
print(str(kss2) + ' kombinacija')
print('garantuje ' + str(k2) + ' pogodaka od ' + str(n2) + ' izvucenih brojeva')
print('za LOTO ' + str(k1) + ' od ' + str(n1))
print()
print()
print('ENTER for EXIT')
print(repr('stop'))
stop = input().strip()
print()
print()
print()


"""
(n1=13, k1=7, n2=7, k2=5)

_______LOTO skraceni sistemi_______

LotoSS.py              ver 1.130812

minimalni broj kombinacija skracenog sistema
i punog sistema
za bilo koju igru LOTO
za bilo koju garanciju

Hypergeometric distribution   h(k2,n2,k1,n1)


UKUPNO BROJEVA:                         n1 = 
13
BROJEVA U KOMBINACIJI (k1<=n1): k1 = 
7
POGODJENIH BROJEVA (n2<=k1):            n2 = 
7
GARANCIJA OD POGODJENIH (k2<=n2):       k2 = 
5

h = 0.183566

verovatnoca:   18.3566 % 

minimalni broj kombinacija skracenog sistema:   5.45


5.45 kombinacija
garantuje 5 pogodaka od 7 izvucenih brojeva
za LOTO 7 od 13


ENTER for EXIT
'stop'
"""


########################################################


"""
(n1=21, k1=7, n2=7, k2=7)

7/7 za 21 
— h             9e-06 

7/7 za 21       
- verovatnoća   0.0009% 

7/7 za 21       
— kombinacija   116280.0




_______LOTO skraceni sistemi_______

LotoSS.py              ver 1.130812

minimalni broj kombinacija skracenog sistema
i punog sistema
za bilo koju igru LOTO
za bilo koju garanciju

Hypergeometric distribution   h(k2,n2,k1,n1)


UKUPNO BROJEVA:                         n1 = 
21
BROJEVA U KOMBINACIJI (k1<=n1): k1 = 
7
POGODJENIH BROJEVA (n2<=k1):            n2 = 
7
GARANCIJA OD POGODJENIH (k2<=n2):       k2 = 
7

h = 9e-06

verovatnoca:   0.0009 % 

minimalni broj kombinacija skracenog sistema:   116280.0


116280.0 kombinacija
garantuje 7 pogodaka od 7 izvucenih brojeva
za LOTO 7 od 21


ENTER for EXIT
'stop'
"""





"""
(n1=21, k1=7, n2=7, k2=5)

5/7 za 21 
— h             0.016434 

5/7 za 21 
— verovatnoća   1.6434% 

5/7 za 21 
— kombinacija   60.85 




_______LOTO skraceni sistemi_______

LotoSS.py              ver 1.130812

minimalni broj kombinacija skracenog sistema
i punog sistema
za bilo koju igru LOTO
za bilo koju garanciju

Hypergeometric distribution   h(k2,n2,k1,n1)


UKUPNO BROJEVA:                         n1 = 
21
BROJEVA U KOMBINACIJI (k1<=n1): k1 = 
7
POGODJENIH BROJEVA (n2<=k1):            n2 = 
7
GARANCIJA OD POGODJENIH (k2<=n2):       k2 = 
5

h = 0.016434

verovatnoca:   1.6434 % 

minimalni broj kombinacija skracenog sistema:   60.85


60.85 kombinacija
garantuje 5 pogodaka od 7 izvucenih brojeva
za LOTO 7 od 21


ENTER for EXIT
'stop'

"""






"""
Formula u kodu je standardna hipergeometrijska PMF za tačno k2 pogodaka.

h = C(k1,k2) * C(n1-k1, n2-k2) / C(n1,n2)

gde je:
C(n,k) = n! / (k! * (n-k)!)



n1 = ukupno brojeva
k1 = brojeva u kombinaciji
n2 = izvučenih brojeva
k2 = tačno pogodjenih brojeva
"""






from math import comb
from fractions import Fraction

def h(n1,k1,n2,k2):
    if k2 < 0 or k2 > k1 or k2 > n2 or n2-k2 > n1-k1:
        return Fraction(0,1)
    return Fraction(comb(k1,k2)*comb(n1-k1,n2-k2), comb(n1,n2))

cases=[
    (13,7,7,5),
    (21,7,7,7),
    (21,7,7,5),
    (39,7,7,4),
    (39,7,7,7),
]

print()
print()
for n1,k1,n2,k2 in cases:
    x=h(n1,k1,n2,k2)
    print((n1,k1,n2,k2), 'h=', float(x), 'percent=', float(x*100), '1/h=', float(1/x) if x else None, 'fraction=', x)
print('at least 5 for 21/7/7:', float(sum(h(21,7,7,k) for k in range(5,8))), '1/sum=', float(1/sum(h(21,7,7,k) for k in range(5,8))))
print()
"""
(13, 7, 7, 5) h= 0.18356643356643357 percent= 18.356643356643357 1/h= 5.447619047619048 fraction= 105/572
(21, 7, 7, 7) h= 8.599931200550395e-06 percent= 0.0008599931200550396 1/h= 116280.0 fraction= 1/116280
(21, 7, 7, 5) h= 0.016434468524251806 percent= 1.6434468524251806 1/h= 60.84772370486656 fraction= 637/38760
(39, 7, 7, 4) h= 0.011286698593200141 percent= 1.1286698593200142 1/h= 88.59986751152074 fraction= 173600/15380937
(39, 7, 7, 7) h= 6.501554489170588e-08 percent= 6.501554489170588e-06 1/h= 15380937.0 fraction= 1/15380937 PUN SISTEM
at least 5 for 21/7/7: 0.017285861713106296 1/sum= 57.850746268656714
"""




"""
Program računa donju granicu (teorijski minimum) broja kombinacija skraćenog sistema (lottery wheel). 
Sistem od n1 brojeva, kombinacija ima k1 brojeva, izvuče se n2 brojeva, a garancija je k2 pogodaka.

h = C(k1,k2)·C(n1−k1, n2−k2) / C(n1,n2)

Pa je:

1/h = C(n1,n2) / [ C(k1,k2)·C(n1−k1, n2−k2) ] = minimalni broj kombinacija (donja granica pokrivanja)





To je teoretski minimum, ali u praksi realan skraćeni sistem (greedy covering), ima vise kombinacija nego teoretski minimum.
Na sajtu https://www.lotoss.info mozete naci realan npr. skraceni sistem sa 10 kombinacija za (13,7,7,5), sto je trenutno svetski rekord. 
Ima i niz drugih skracenih sistema sto su svetski rekordi. 

Formulom se racuna donja granica pokrivanja, a onda treba generisati skraceni sistem koji tome tezi. 

Npr. Schönheim granica:

L ≥ ⌈ n1/k1 · ⌈ (n1−1)/(k1−1) · … · ⌈ (n1−k2+1)/(k1−k2+1) ⌉ … ⌉ ⌉





Teorijski minimum / donja granicu broja kombinacija skraćenog sistema kroz hipergeometrijski odnos. 
Primer punog sistema (39,7,7,7) daje 1/h = 15,380,937, što je tačno C(39,7).
Za (13,7,7,5) formula daje oko 5.45 (donja granica → 6 kao apsolutni pod), dok moj sistem ima 10 kombinacija.
LotoSS.py je ispravan kao kalkulator teorijskog minimuma, ali nije generator skraćenih sistema. 
Ozbiljan korak bi bio poseban kod koji generiše i proverava skracenesisteme (i njihove vezane dobitke).
"""
