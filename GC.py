def GCcontent(dna):
	count = 0
	dna_len = float(len(dna))
	for n in dna:
		if n in ['G', 'C']:
			count = count + 1
	content = (float(count)/dna_len)
	return content * 100

with open("data.txt", "r") as f:
	lines = f.readlines()
	num_of_lines = len(lines)
	ans = 0.0
	label = ''
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
		loc_ans = GCcontent(dna)
		if loc_ans > ans:
			ans = loc_ans
			label = loc_label

print label.strip('>'), ans
