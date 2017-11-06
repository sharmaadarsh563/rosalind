# A measure of gene order similarity

# Say that two chromosomes share n genes; if we label the genes of one chromosome
# by the numbers 1 through n in the order that they appear, then the second chromosome
# will be given by a permutation of these numbered genes. To find the largest number
# of genes appearing in the same order, we need only to find the largest collection of
# increasing elements in the permutation.

import copy
from settings import BASE_DIR

def __lgis(seq, num):
	if not isinstance(seq, list) or\
	 not isinstance(num, int):
		raise Exception(
			"Data is corrupted! Please provide input.")
	liss, ldss = [[]]*num, [[]]*num

	# initializing lists of longest increasing/decreasing
	# subsequence ending at element with index 'i'
	for i in range(0, num):
		liss[i], ldss[i] = [seq[i]], [seq[i]]

	# generating lists of longest increasing subsequence
	# ending at element with index 'i'
	for i in range(1, num):
		for j in range(0, i):
			prefix_seq = copy.copy(liss[j])
			if seq[i] > seq[j] and len(liss[i]) < len(liss[j]) + 1:
				prefix_seq.append(seq[i])
				liss[i] = prefix_seq

	# generating lists of longest decreasing subsequence
	# ending at element with index 'i'
	for i in range(1, num):
		for j in range(0, i):
			prefix_seq = copy.copy(ldss[j])
			if seq[i] < seq[j] and len(ldss[i]) < len(ldss[j]) + 1:
				prefix_seq.append(seq[i])
				ldss[i] = prefix_seq

	# finding longest increasing/decreasing subsequence
	max_liss, max_ldss = [], []
	for i in range(num):
		if len(liss[i]) > len(max_liss):
			max_liss = liss[i]
		if len(ldss[i]) > len(max_ldss):
			max_ldss = ldss[i]

	return max_liss, max_ldss

if __name__ == "__main__":
	try:
		f = open(BASE_DIR + "LGIS.txt", "r")
		lines = f.readlines()
		f.close()
		num = int(lines[0])
		seq = map(int, lines[1].split(" "))
		max_liss, max_ldss = __lgis(seq, num)

		# print longest increasing subsequence
		for i in range(len(max_liss)-1):
			print str(max_liss[i])+" ",
		print str(max_liss[len(max_liss)-1])

		# print longest decreasing subsequence
		for i in range(len(max_ldss)-1):
			print str(max_ldss[i])+" ",
		print str(max_ldss[len(max_ldss)-1])
	except Exception as e:
		print "Error while find gene order similarity! -- {}".format(str(e))