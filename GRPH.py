seqs = {}
with open("data.txt", "r") as f:
	lines = f.readlines()
	num_of_lines = len(lines)
	i = 0			
	while i < num_of_lines and lines[i][0] == '>':
		label = lines[i][1:].strip('\n')
		i += 1
		dna = ''
		while i < num_of_lines and lines[i][0] != '>':
			dna += lines[i].strip('\n')
			i += 1
		seqs[label] = dna


labels = seqs.keys()
for i in range(len(labels)):
	for j in range(len(labels)):
		if i != j and (seqs[labels[i]][-3:] == seqs[labels[j]][:3]):
			print labels[i] + " " + labels[j]


