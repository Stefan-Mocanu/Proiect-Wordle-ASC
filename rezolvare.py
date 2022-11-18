import random
f=open("cuvinte.txt", "r")
L=f.read()
f.close()
L=L.split("\n")
L=L[:-1]
Cuvinte=L
rez=""
def give_best():
	global lit
	global Cuvinte
	d=[{chr(x):0 for x in range(ord('A'),ord('Z')+1)} for i in range(5)]
	for i in range(len(Cuvinte)):
		for poz in range(5):
			aux=Cuvinte[i][poz]
			d[poz][aux]+=1
	best=''
	score=0
	max_score=0
	for i in range(len(Cuvinte)):
		for poz in range(5):
			aux=Cuvinte[i][poz]
			score+=d[poz][aux]
		if score>max_score:
			max_score=score
			best=Cuvinte[i]
		score=0
	return best

def schimba(rez, sol):
	global lit
	global Cuvinte
	Cuvinte.remove(sol)
	for i in range(5):
		if rez[i]=="🟩":
			for j in Cuvinte:
				if j==sol[i]:
					Cuvinte.remove(j)
		if rez[i]=="🟨":
			for j in Cuvinte:
				if sol[i] not in j or j[i]==sol[i]:
					Cuvinte.remove(j)
		if rez[i]=="⬜":
			for j in Cuvinte:
				if j[i]==sol[i]:
					Cuvinte.remove(j)



ok=False
while ok!=True:
	f=open("IO1.txt","w")
	solutie=give_best()
	print("Ghicire", solutie)
	f.write(solutie)
	f.close()
	g=open("IO2.txt","r")
	while True:
		rez=g.read()
		if rez!='':
			break
	g.close()
	print("Primit",rez)
	g=open("IO2.txt","w")
	g.close()
	if rez=="🟩🟩🟩🟩🟩":
		ok=True
		continue
	schimba(rez,solutie)
	rez=""
	
