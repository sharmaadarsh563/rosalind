
BASE_DIR = "datasets/"

DNA_PROT_MAP = {"TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V", "TTC": "F", "CTC": "L",
                "ATC": "I", "GTC": "V", "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
                "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V", "TCT": "S", "CCT": "P",
                "ACT": "T", "GCT": "A", "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A", "TCG": "S", "CCG": "P",
                "ACG": "T", "GCG": "A", "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
                "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "TAA": None, "CAA": "Q",
                "AAA": "K", "GAA": "E", "TAG": None, "CAG": "Q", "AAG": "K", "GAG": "E",
                "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G", "TGC": "C", "CGC": "R",
                "AGC": "S", "GGC": "G", "TGA": None, "CGA": "R", "AGA": "R", "GGA":"G",
                "TGG": "W", "CGG": "R", "AGG": "R", "GGG":"G"}

MONOISOTOPIC_MASSES = {
        'A':   71.03711,
        'C':   103.00919,
        'D':   115.02694,
        'E':   129.04259,
        'F':   147.06841,
        'G':   57.02146,
        'H':   137.05891,
        'I':   113.08406,
        'K':   128.09496,
        'L':   113.08406,
        'M':   131.04049,
        'N':   114.04293,
        'P':   97.05276,
        'Q':   128.05858,
        'R':   156.10111,
        'S':   87.03203,
        'T':   101.04768,
        'V':   99.06841,
        'W':   186.07931,
        'Y':   163.06333
}

NUC_NUM_MAPPING = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

NUM_NUC_MAPPING = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

STOP_CODONS = ["TAG", "TGA", "TAA"]

TEMP_DIR = "/tmp/"
