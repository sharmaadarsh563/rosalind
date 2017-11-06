# ASSUMPTION: There exists a unique way to reconstruct the entire
#             chromosome from these reads by gluing together pairs
#             of reads that overlap by more than half their length
from settings import BASE_DIR


class Read(object):
	"""
	A read's representation
	"""

	def __init__(self, data):
		# actual sequence
		self.read = data
		# whether this read has been used to
		# assemble DNA
		self.consumed = False

def getReads(file):
	reads = []
	if not file:
		return reads
	try:
		with open(file, "r") as f:
			lines = f.readlines()
			num_of_lines = len(lines)
			i = 0
			while i < num_of_lines and lines[i][0] == '>':
				read = ''
				i += 1
				while i < num_of_lines and lines[i][0] != '>':
					read += lines[i].strip('\n')
					i += 1
				reads.append(Read(read))
	except Exception as e:
		raise Exception(str(e))
	return reads

# Time-complexity: O(length of read), as each read's letter is
#                  parsed only once
def getPrefixEndIndex(dna, read):
	if not isinstance(dna, basestring) or\
	 not isinstance(read, basestring):
		return -1

	read_len = len(read)
	dna_len = len(dna)

	prev_read_len = read_len
	prefix_end_index = -1
	read_index = read_len - 1
	dna_index = dna_len - 1
	while read_index >= 0:
		if read[read_index] == dna[dna_index]:
			if prefix_end_index == -1:
				prefix_end_index = read_index
			read_index -= 1
			dna_index -= 1
		else:
			prev_read_len -= 1
			prefix_end_index = -1
			dna_index = dna_len - 1
			read_index = prev_read_len - 1
	return prefix_end_index


# Time-complexity: O(length of read), as each read's letter is
#                  parsed only once
def getSuffixStartIndex(dna, read):
	if not isinstance(dna, basestring) or\
	 not isinstance(read, basestring):
		return -1

	read_len = len(read)
	dna_len = len(dna)

	suffix_start_index = -1
	read_index = 0
	dna_index = 0
	while read_index < len(read):
		if read[read_index] == dna[dna_index]:
			if suffix_start_index == -1:
				suffix_start_index = read_index
			read_index += 1
			dna_index += 1
		else:
			dna_index = 0
			if suffix_start_index != -1:
				read_index = suffix_start_index + 1
			else:
				read_index += 1
			suffix_start_index = -1
	return suffix_start_index

# Time-complexity: O(length of read)
def midOverlap(dna, read):

	if not isinstance(dna, basestring) or\
	 not isinstance(read, basestring):
		return (dna, True)

	# check for read's prefix as dna's suffix
	prefix_end_index = getPrefixEndIndex(dna, read)

	if prefix_end_index >= len(read)/2:
		dna += read[prefix_end_index+1:]
		return (dna, True)

	# check for read's suffix as dna's prefix
	suffix_start_index = getSuffixStartIndex(dna, read)

	if suffix_start_index >= 0 and (len(read) - suffix_start_index)\
	 >= len(read)/2:
		dna = read[:suffix_start_index] + dna
		return (dna, True)

	return (dna, False)

def assembleReads(reads):
	if not reads or not isinstance(reads, list):
		return ""
	dna = reads[0].read
	reads[0].consumed = True

	while True:
		flag = True
		for i in range(1, len(reads)):
			if not reads[i].consumed:
				flag = False
				dna, status = midOverlap(dna, reads[i].read)
				if status:
					reads[i].consumed = True
		if flag:
			break

	return dna


if __name__ == "__main__":
	try:
		reads = getReads(BASE_DIR + "LONG.txt")
		print assembleReads(reads)
	except Exception as e:
		print "Error is assembling reads! -- {}".format(str(e))