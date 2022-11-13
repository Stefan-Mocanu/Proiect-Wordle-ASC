import random
f=open("cuvinte.txt", "r")
L=f.read()
f.close()
L=L.split("\n")
Cuvinte=L
lit={chr(x):1 for x in range(ord('A'),ord('Z')+1)}

def give_best():
	global lit,Cuvinte
	d=[{chr(x):0 for x in range(ord('A'),ord('Z')+1) if lit[chr(x)]==1} for i in range(5)]
	for elem in Cuvinte:
		for poz in range(5):
			aux=elem[poz]
			d[poz][aux]+=1
	best=''
	score=0
	max_score=0
	for elem in Cuvinte:
		for poz in range(5):
			aux=elem[poz]
			score+=d[poz][aux]
		if score>max_score:
			max_score=score
			best=elem
	return best
#ok=False
#while ok!=True
	#f=open("IO1.txt","w")
print(give_best())
	#f.close()
	#g=open("IO2.txt","r")
	#rez=g.read()
	#g.close()
	#schimba(rez)
