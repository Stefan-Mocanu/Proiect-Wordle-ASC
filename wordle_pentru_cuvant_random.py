import random
f=open("cuvinte.txt", "r")
L=f.read()
f.close()
L=L.split("\n")
L=L[:-1]

cuv=L[random.randint(0,11455)]
guess=''
nr=1
while guess!=cuv:
	f=open("IO1.txt","r")
	while True:
		guess=f.read()
		if guess!="":
			break
	f.close()
	print("Incercare", guess)
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
	print(status)
	g.write(status)
	g.close()
	if status=="🟩🟩🟩🟩🟩":
		print(f"Cuvantul {cuv} a fost ghicit in {nr} incercari")
		break
	else:
		nr+=1
	guess=""

