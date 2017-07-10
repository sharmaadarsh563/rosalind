import numpy
profile = numpy.zeros((4, 1001))

nuc_num_mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
num_nuc_mapping = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
dna_len = 0

def updateProfile(dna):
	for i in range(len(dna)):
		profile[nuc_num_mapping[dna[i]]][i] += 1.0
	return

with open("data.txt", "r") as f:
	lines = f.readlines()
	num_of_lines = len(lines)
	i = 0
	while lines[i][0] != '>':
		i += 1
	while i < num_of_lines and lines[i][0] == '>':
		loc_label = lines[i]
		i += 1
		dna = ''
		while i < num_of_lines and lines[i][0] != '>':
			dna += lines[i].strip('\n')
			i += 1
		dna_len = len(dna)
		updateProfile(dna)

f = open("ans.text", "w")
consensus = ''
for i in range(1001):
	max_freq = 0
	freq_nucl = ''
	for j in range(4):
		if profile[j][i] > max_freq:
			max_freq = profile[j][i]
			freq_nucl = num_nuc_mapping[j]
	consensus += freq_nucl

f.write(consensus+"\n")

for i in range(4):
	f.write(num_nuc_mapping[i]+": ")
	for j in range(dna_len-1):
		f.write(str(int(profile[i][j]))+" ")
	f.write(str(int(profile[i][j+1]))+"\n")
f.close()