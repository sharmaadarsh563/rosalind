from settings import BASE_DIR

def __estimate(dna):
	"""
	estimating...
	"""
	if not isinstance(dna, basestring):
		raise Exception("Invalid DNA!")
	count = 0
	dna_len = float(len(dna))
	for n in dna:
		if n in ['G', 'C']:
			count = count + 1
	content = (float(count)/dna_len)
	return content * 100


def estimateGCcontent(filename):
	"""
	reading data from file, then estimating GC content in DNA
	"""
	try:
		with open(filename, "r") as f:
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
				loc_ans = __estimate(dna)
				if loc_ans > ans:
					ans = loc_ans
					label = loc_label

		print label.strip('>'), ans
	except Exception as e:
		raise Exception(str(e))

if __name__ == "__main__":
	try:
		estimateGCcontent(BASE_DIR + "GC.txt")
	except Exception as e:
		print "Error in estimating GC content! -- {}".format(str(e))
