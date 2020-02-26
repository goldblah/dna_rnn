from random import randint

#concatenate fasta files
def linearize_genome(filename):
	linear_genome=""
	bad_words=['>',' ']
	with open(filename) as genome_fasta:
		for line in genome_fasta:
			if not any(bad_word in line for bad_word in bad_words):
				linear_genome+=line
	return(linear_genome)

def sample_genome(sample_number, sample_length, linearized_genome):
	#sample_number = integer of desired samples
	#sample_length = integer of desired sample size
	#linearized_genome = string of DNA sequence without '>' or empty lines. produced by function linearize_genome
	
	#get length of genome
	genome_length = len(linearized_genome)
	#store output as list of lists. Change if needed
	random_dna_list =[]
	for i in range(sample_number):
		succesful_sample = False
		while not succesful_sample:
			random_start = randint(0, genome_length)
			if random_start + sample_length > genome_length:
				continue
			else:
				random_sequence = linearized_genome[random_start:random_start + sample_length]
				random_dna_list.append(random_sequence)
				succesful_sample = True
	return(random_dna_list)
