# read a standard .fsa genetic code chromosome text file, remove the first line of non-sequence text
# remove the newlines to make a single string of atcg sequence
# replace the atcg with base 4 bits 00 thru 11
# write the bit file to a new text file

with open('chr01.fsa') as f:
	seq_join = ""
	next(f)
	for line in f:
		stripped_line = line.rstrip()
		seq_join += stripped_line
seq = seq_join.lower()
seq = seq.replace('c', '00').replace('g','01').replace('a','10').replace('t','11')
#print(seq_join)

print(seq)
with open('chr01.txt', 'w') as n:
    n.write(seq)

