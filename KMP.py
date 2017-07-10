# get longest prefix and corresponding matching suffix
# according to KMP Algorithm
def get_lps(dna):
	dna_len = len(dna)
	lps = [0] * dna_len
	lps_len = 0
	i = 1
	while i < dna_len:
		if dna[lps_len] == dna[i]:
			lps_len += 1
			lps[i] = lps_len
			i += 1
		else:
			if lps_len != 0:
				lps_len = lps[lps_len-1]
			else:
				lps_len = 0
				i += 1
	return lps

lps = []
with open("data.txt", "r") as f:
	lines = f.readlines()
	num_of_lines = len(lines)
	if lines[0][0] == '>':
		dna = ''
		i = 1
		while i < num_of_lines and lines[i][0] != '>':
			dna += lines[i].strip('\n')
			i += 1
		lps = get_lps(dna)

f = open("ans.text", "w")
for i in range(len(lps)):
	f.write(str(lps[i])+" ")

f.close()
