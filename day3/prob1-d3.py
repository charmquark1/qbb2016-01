import sys
import fasta_fixed

kmer_dic={}

#i have the kmer at position i, if ive seen the kmer, it sets to 0. if i have seen it, 
# define target name from subset target file. sys.stdin is subset

# Take query file. 
# Define k-mer sequence in query. AAATCTAGT
# Define query_start as cursor to [0]
# Then search for string in target
# When found, calculate distance between hit and start (sequence[0]), define as target_start


for ident, sequence in fasta_fixed.FASTAReader(target):
    sequence = sequence.upper()
    for i in range(0, len(sequence)-k):
        kmer = sequence[i: i+k]
        if kmer not in kmercounts:
            kmercounts[kmer] = 0
        kmercounts[kmer] += 1
    print "---", ident, "---
print ident+"\t"+sequence[**] + "\t" +*** + k
    
target = open(sys.argv[1])
query = open(sys.argv[2])

------------
import sys, fasta
 
target = open(sys.argv[1])
source = open(sys.argv[2])
lengths = []


k = int(sys.argv[3])
#make a query dictionary
kmer_source = {}

# put query in FASTA reader. spits out gene name and sequence
# when your cursor is within 0 to length (defined by k), 
### kmer is the sequence from cursor to cursor + 11 which defines the kmer)
### if the kmer string is not in the dictionary, add to dictionary 
for ident, sequence in fasta.FASTAReader(source):
    sequence = sequence.upper()
    for i in range(0, len(sequence)-k):
        kmer = sequence[i : i + k]
        if kmer not in kmer_source:
            kmer_source[kmer] = []

        kmer_source[kmer].append(i)

#make target dictionaries
## wh

kmer_position = {}
for ident, sequence in fasta.FASTAReader(target):
    sequence = sequence.upper()
    
    #lets you have empty kmer_counts at start of each sequence
    kmer_position = {}
    #makes each dictionary
    
    for i in range(0, len(sequence)-k):
        kmer = sequence[i : i + k]
        if kmer not in kmer_position:
            kmer_position[kmer] = []
 
        kmer_position[kmer].append(i)
    #checks dictionaries against each other and prints out the corresponding values

    for kmer in kmer_position:

        if kmer in kmer_source:
            print "---target sequence name: " + ident + "---\t" + "target starts:\t" + str(kmer_position[kmer]) + "\tquery starts:\t" + str(kmer_source[kmer]) + "\tkmer:\t" + kmer

