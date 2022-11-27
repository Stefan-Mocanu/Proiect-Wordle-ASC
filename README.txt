Autorii proiectului
Mocanu Ștefan, grupa 133
Ciobanu Ioan-Paul, grupa 133

Programul rezolvare calculează pentru fiecare cuvânt probabiltatea de apariție ca feedback a fiecărei distribuții de semnale verde, galben si gri. Entropia cuvântului se calculeaza pe baza acestor probabilități. Iar probabiltiatea fiecărei distribuții se calculează comparând cuvântul cu toate cuvintele care au mai ramas ca posibile solutii.
Cuvântul optim este ales ca input pentru programul wordle, și în baza feedback-ului din programul wordle,rezolvare elemină cuvintele care nu pot fi soluții. 

Pentru eficiența din punct de vedere a timpului de executare s-a calculat entropia fiecărui cuvânt o dată, cuvântul cu entropia maximă este TAREI, iar fiecare cuvânt împreună cu entropiile lor au fost salvate în fișierul entropie.txt.

Programele wordle.py și rezolvare.py numără încercările necesare pentru fiecare cuvânt.
Pentru executare s-a folosit comanda din terminalul Linux:
python3 wordle.py &python3 rezolvare.py

Programele wordle_pentru_cuvant_random.py si rezolvare_pentru_cuvant_random.py numără 
încercările necesare pentru un cuvănt random.
Pentru executare s-a folosit comanda din terminalul Linux:
python3 wordle_pentru_cuvant_random.py &python3 rezolvare_pentru_cuvant_random.py

Comunicarea între programe se face prin intermediul fișierelor IO1.txt și IO2.txt.

În medie a fost nevoie de 4.374105116116641 soluții pentru ghicirea tuturor cuvintelor.

Referințe:
Entropia lui Shannon: Cursul 0x02, Arhitectura Sistemelor de calcul
https://cs.unibuc.ro/~crusu/asc/Arhitectura%20Sistemelor%20de%20Calcul%20(ASC)%20-%20Curs%200x02.pdf

Algoritmul de calculare a cuvantului optim:
https://www.youtube.com/watch?v=v68zYyaEmEA
