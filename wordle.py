import random
f=open("cuvinte.txt", "r")
L=f.read()
L=L.split("\n")

cuv=L[random.randint(0,11455)]
print(cuv)
guess=''
while guess!=cuv:
	guess=input("Ghiciti: ")
	status=''
	for index in range(len(guess)):
		if guess[index]==cuv[index]:
			status+="🟩"
		elif guess[index] in cuv:
			status+="🟨"
		else:
			status+="⬜"
	print(status)
