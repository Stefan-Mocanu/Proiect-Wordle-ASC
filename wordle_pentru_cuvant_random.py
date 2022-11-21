import random
f=open("cuvinte.txt", "r")
L=f.read()
f.close()
L=L.split("\n")
L=L[:-1]

cuv=L[random.randint(0,11455)]
print(cuv)
guess=''
nr=0
while guess!=cuv:
	f=open("IO1.txt","r")
	while True:
		guess=f.read()
		if guess!="":
			break
	f.close()
	print("Primit", guess)
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
		print(nr)
		break
	else:
		nr+=1
	guess=""

