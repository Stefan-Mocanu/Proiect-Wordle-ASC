import math
f=open("cuvinte.txt", "r")
L=f.read()
f.close()
L=L.split("\n")
L=L[:-1]
Cuvinte=L.copy()
rez=""
lun=len(L)
def give_best():
	global Cuvinte
	lun = len(Cuvinte)
	if lun == 1:
		return Cuvinte[0]
	maxe = 0
	maxguess = ""
	for guess in L:
		d = {}
		for sol in Cuvinte:
			distrib = []
			for i in range(5):
				if guess[i] == sol[i]:
					distrib.append("🟩")
				elif guess[i] in sol:
					distrib.append("🟨")
				else:
					distrib.append("⬜")
			distrib = tuple(distrib)
			if distrib in d:
				d[distrib] += 1
			else:
				d[distrib] = 1
		E = 0
		for distrib in d:
			p = d[distrib] / lun
			E += -p * math.log2(p)
		if E > maxe:
			maxe = E
			maxguess = guess
	return maxguess


def schimba(rez, sol):
	global Cuvinte
	if sol in Cuvinte:
		Cuvinte.remove(sol)
	for i in range(5):
		if rez[i]=="🟩":
			j = 0
			while j < len(Cuvinte):
				if Cuvinte[j][i]!=sol[i]:
					Cuvinte.remove(Cuvinte[j])
				else:
					j += 1
		if rez[i]=="🟨":
			j = 0
			while j < len(Cuvinte):
				if sol[i] not in Cuvinte[j] or Cuvinte[j][i]==sol[i]:
					Cuvinte.remove(Cuvinte[j])
				else:
					j += 1
		if rez[i]=="⬜":
			j = 0
			while j < len(Cuvinte):
				if sol[i] in Cuvinte[j]:
					Cuvinte.remove(Cuvinte[j])
				else:
					j += 1
					
for index in range(lun):
	ok=False
	Cuvinte=L.copy()
	rez=""
	i=1
	while ok!=True:
		f=open("IO1.txt","w")
		if i == 1:
			solutie = "TAREI"
		else:
			solutie = give_best()
		f.write(solutie)
		f.close()
		g=open("IO2.txt","r")
		while True:
			rez=g.read()
			if rez!='':
				break
		g.close()
		g=open("IO2.txt","w")
		g.close()
		if rez=="🟩🟩🟩🟩🟩":
			ok=True
			continue
		schimba(rez,solutie)
		rez=""
		i+=1
	
		
