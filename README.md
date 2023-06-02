## Bioinformatics

The ideia of this repository is to learn and add some code I am thinking about and creating. The basic starting ideia is playing a little bit with genomics, lists tuples, dictionaries and text in Python. In the future 
my plan is to add some data science stuff as well, when I learn it properly (or not so much).



1) [counting_nucleotides.py] The first code I have added was my solution for a counting nucleotide problem at https://rosalind.info/problems/dna/ . It's a general purpose program to count nucleotides within a .txt file or given by the user in python. 

2) [dna_to_rna] The second code is the resolution of the exercise that can be found here: https://rosalind.info/problems/rna/ . The idea was pretty simple, just changing the T's on the code for U's. 

3) [complementary_strand] Now the game was put in a higher stantard. I had to solve how to make an inverted strant and at the same time, translate it. I have used slicing methods that I have learned just to it, and also came with the problem to translate the code without changing former changes. The challenge can be found here: https://rosalind.info/problems/revc/ . 

4) [counting_gc_content] Ok, this on was hard for me. The ideia is to read a FAST file (it is organized like this: ">'sequence_id"\n<sequence>"*n and the ideia was to isolate it, make the GC content calculation ((G + C) / (G + C + T + A) in a way that the user can know what sequence has the biggest gc content. I know there are cleaner ways of solving it but this is what I can do in my current experience in python.  
