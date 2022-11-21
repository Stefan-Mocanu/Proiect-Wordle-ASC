import random
f=open("cuvinte.txt", "r")
L=f.read()
f.close()
L=L.split("\n")
L=L[:-1]
lun=len(L)
medie=0.0
nr=0
for cuv in L:
	list=[cuv]
	nr=0
	guess=''
	while guess!=cuv:
		f=open("IO1.txt","r")
		while True:
			guess=f.read()
			if guess!="":
				break
		f.close()
		list.append(guess)
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
	f=open("solutii.txt","a")
	f.write(", ".join(list))
	f.write("\n")
	f.close()
	print(f"Pentru {cuv} a fost nevoie de {nr} incercari")
	medie+=nr
medie=medie/lun
print(f"In medie a fost nevoie de {medie} incercari")

