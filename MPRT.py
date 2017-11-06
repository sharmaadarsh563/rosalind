import requests
from settings import BASE_DIR

class SearchProteinMotif(object):
	"""
	class for searching a motif pattern, 'N{P}[ST]{P},' in the
	given protein sequence
	"""

	def __init__(self, motif_len):
		self.pattern_len = motif_len
		self.base_dir = "/tmp/"
		self.uniprot_link = "http://www.uniprot.org/uniprot/"

	def __make_request(self, accession_id):
		response = requests.request(
			"GET", self.uniprot_link + accession_id + ".fasta", timeout=3)
		if response.status_code != 200:
			raise Exception("Error making request to UniProt!")
		return response.content

	def __locations(self, protein_seq):
		locs = []
		if not isinstance(protein_seq, basestring):
			raise Exception("Protein Sequence is missing!")
		protein_len = len(protein_seq)
		for i in range(protein_len-self.pattern_len+1):
			if protein_seq[i]=='N' and protein_seq[i+1]!='P'\
			 and protein_seq[i+2] in ['S', 'T'] and protein_seq[i+3]!='P':
				locs.append(i+1)
		return locs

	def __find_locations(self, accession_ids, fasta_seqs):
		accessions_locs = {}
		try:
			with open(self.base_dir + fasta_seqs, "r") as f_read:
				lines = f_read.readlines()
				num_of_lines = len(lines)
				counter=0
				protein_seq=''
				for i in range(num_of_lines):
					if lines[i][0] == '>':
						if protein_seq:
							locs = self.__locations(protein_seq)
							accessions_locs[accession_ids[counter-1]] = locs
						protein_seq = ''
						counter+=1
					else:
						protein_seq += lines[i].strip('\n')
				if protein_seq:
					locs = self.__locations(protein_seq)
					accessions_locs[accession_ids[counter-1]] = locs
		except Exception as e:
			raise Exception(str(e))
		return accessions_locs

	def search(self):
		fasta_seqs = "fasta_seqs.txt"
		try:
			f_write = open(self.base_dir + fasta_seqs, "w")
			with open(BASE_DIR + "MPRT.txt", "r") as f_read:
				lines = f_read.readlines()
				accession_ids = []
				for line in lines:
					accession_id = line.strip('\n')
					accession_ids.append(accession_id)
					fasta_seq = self.__make_request(accession_id)
					f_write.write(fasta_seq)
			f_write.close()
			print self.__find_locations(accession_ids, fasta_seqs)
		except Exception as e:
			print "Error while searching the motif! -- {}".format(str(e))

if __name__ == "__main__":
	spm = SearchProteinMotif(4)
	spm.search()