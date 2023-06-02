def counting_mutations(sequence1, sequence2): #this function compares 2 lists telling the # of times they're different
	
	hd = 0 #Hamming Distance 
	i = 0
	for nuc in sequence1:
		if sequence1[i] == sequence2[i]:
			hd += 0
		else:
			hd += 1
		i += 1
	return hd
	
dir_pathway = input('Type the file pathway: ') #asking for the pathway

sequences_txt = open(dir_pathway, 'r')
sequences = sequences_txt.read()
sequences_list = sequences.split('\n', 1) #formating the file

sequence1 = sequences_list[0] #dividing the sequences
sequence2 = sequences_list[1]

hd = counting_mutations(sequence1, sequence2) #comparing the sequences

print(f'The number of sigle mutations comparing the 2 strands is: {hd}') #output and result


sequences_txt.close()
