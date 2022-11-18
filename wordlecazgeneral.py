import random
f=open("cuvinte.txt", "r")
L=f.read()
f.close()
L=L.split("\n")
lun=len(L)
medie=0.0
nr=0
for cuv in L:
	nr=0
	guess=''
	while guess!=cuv:
		f=open("IO1.txt","r")
		while True:
			guess=f.read()
			if guess!="":
				break
		f.close()
		#print("Primit", guess)
		f=open("IO1.txt","w")
		f.close()
		status=''
		for index in range(len(guess)):
			if guess[index]==cuv[index]:
				status+="🟩"
			elif guess[index] in cuv:
				status+="🟨"
			else:
				status+="⬜"
		g=open("IO2.txt","w")
		g.write(status)
		g.close()
		if status=="🟩🟩🟩🟩🟩":
			nr+=1
			break
		else:
			nr+=1
		guess=""
	print(f"Gasit {cuv} in {nr} incercari")
	medie+=nr
medie=medie/lun
print(f"In medie a fost nevoie de {medie} incercari")

