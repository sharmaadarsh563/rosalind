
from settings import MONOISOTOPIC_MASSES, BASE_DIR

def __peptide_mass(filename):
	"""
	calculating peptide's mass
	"""
	# read and close the file
	f = open(filename, "r")
	lines = f.readlines()
	f.close()

	mass = 0.0
	peptide = lines[0].strip("\n")
	for i in range(0, len(peptide)):
		mass += MONOISOTOPIC_MASSES.get(peptide[i], 0.0)
	return mass

if __name__ == "__main__":
	try:
		print __peptide_mass(BASE_DIR + "PRTM.txt")
	except Exception as e:
		print "Error finding peptide mass! -- {}".format(str(e))
