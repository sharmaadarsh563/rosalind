
def lcsm(protein_seqs):
	protein_seqs.sort(key = lambda seq: len(seq))
	shortest_seq_len = len(protein_seqs[0])
	max_motif = ''
	for l in range(0, shortest_seq_len):
		r = shortest_seq_len-1
		while r >= l:
			found = True
			motif = protein_seqs[0][l:r+1]
			for seq in protein_seqs[1:]:
				if motif not in seq:
					found = False
					break
			if found and len(motif)>=len(max_motif):
				max_motif = motif
				break
			r-=1
	return max_motif

def find_shared_motif():
	f_read = open("datasets/LCSM.txt", "r")
	lines = f_read.readlines()
	f_read.close()
	num_of_lines = len(lines)
	protein_seqs=[]
	seq = ''
	for i in range(num_of_lines):
		if lines[i][0] == '>':
			if seq:
				protein_seqs.append(seq)
			seq = ''
		else:
			seq += lines[i].strip('\n')
	if seq:
		protein_seqs.append(seq)
	print lcsm(protein_seqs)

if __name__ == "__main__":
	find_shared_motif()