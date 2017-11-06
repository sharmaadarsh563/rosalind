import numpy
from settings import BASE_DIR, NUC_NUM_MAPPING, NUM_NUC_MAPPING, TEMP_DIR

def __create(dna, profile):
	"""
	creating profile
	"""
	if not isinstance(dna, basestring) or\
	 not isinstance(profile, (numpy.ndarray, numpy.generic)):
		raise Exception("Input data is corrupted or invalid!")
	for i in range(len(dna)):
		profile[NUC_NUM_MAPPING[dna[i]]][i] += 1.0
	return

def createProfile(filename):
	"""
	reading input, before creating profile
	"""
	profile = numpy.zeros((4, 1001))
	dna_len = 0
	try:
		with open(filename, "r") as f:
			lines = f.readlines()
			num_of_lines = len(lines)
			i = 0
			while lines[i][0] != '>':
				i += 1
			while i < num_of_lines and lines[i][0] == '>':
				i += 1
				dna = ''
				while i < num_of_lines and lines[i][0] != '>':
					dna += lines[i].strip('\n')
					i += 1
				if not dna_len:
					dna_len = len(dna)
				__create(dna, profile)
	except Exception as e:
		raise Exception(str(e))
	return (profile, dna_len)

def showConsensusProfile(profile, dna_len):
	"""
	print consensus sequence and profile matrix
	"""
	if not isinstance(dna_len, int) or\
	 not isinstance(profile, (numpy.ndarray, numpy.generic)):
		raise Exception("Invalid profile or dna's length!")
	try:
		f = open(TEMP_DIR + "CONS_output.text", "w")
		consensus = ''
		for i in range(1001):
			max_freq = 0
			freq_nucl = ''
			for j in range(4):
				if profile[j][i] > max_freq:
					max_freq = profile[j][i]
					freq_nucl = NUM_NUC_MAPPING[j]
			consensus += freq_nucl

		f.write(consensus+"\n")

		for i in range(4):
			f.write(NUM_NUC_MAPPING[i]+": ")
			for j in range(dna_len-1):
				f.write(str(int(profile[i][j]))+" ")
			f.write(str(int(profile[i][j+1]))+"\n")
		f.close()
	except Exception as e:
		raise Exception(str(e))

if __name__ == "__main__":
	try:
		profile, dna_len = createProfile(BASE_DIR + "CONS.txt")
		showConsensusProfile(profile, dna_len)
	except Exception as e:
		print "Error is assembling reads! -- {}".format(str(e))
