from random import randint
import numpy as np

#concatenate fasta files
def linearize_genome(filename):
	linear_genome=""
	bad_words=['>',' ']
	with open(filename) as genome_fasta:
		for line in genome_fasta:
			if not any(bad_word in line for bad_word in bad_words):
				linear_genome+=line
	return(linear_genome)

# Sample length must be postive integer
# Our distribution has mean 17928.2 and standard deviation 43102.3
def pos_normal(mean, sigma):
    x = random.normalvariate(mean,sigma)
    return(int(x) if x>=0 else PosNormal(mean,sigma))

def sample_genome(sample_number, linearized_genome, length_mean, length_sigma):
	#sample_number = integer of desired samples
	#linearized_genome = string of DNA sequence without '>' or empty lines. produced by function linearize_genome
	
	#get length of genome
	genome_length = len(linearized_genome)
	#store output as list of lists. Change if needed
	random_dna_list =[]
	
	for i in range(sample_number):
		succesful_sample = False
		while not succesful_sample:
			random_start = randint(0, genome_length)
			sample_length = pos_normal(length_mean, length_sigma)
			if random_start + sample_length > genome_length:
				continue
			else:
				random_sequence = linearized_genome[random_start:random_start + sample_length]
				random_dna_list.append(random_sequence)
				succesful_sample = True
	return(random_dna_list)



