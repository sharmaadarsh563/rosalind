import math
dna = raw_input()
gc_conts = map(float, raw_input().split(' '))
ans = [0.0]*len(gc_conts)

for i in range(len(gc_conts)):
	gc_cont = gc_conts[i]/2
	at_cont = (1 - gc_conts[i])/2
	for j in range(len(dna)):
		if dna[j] in ['A', 'T']:
			ans[i] += math.log(at_cont, 10)
		else:
			ans[i] += math.log(gc_cont, 10)

print ans