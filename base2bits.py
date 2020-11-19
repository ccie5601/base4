#using cg as the 00-01 base - 
#  c = 00
#	g = 01
#using at as the 10-11 base
#	a = 10
#	t = 11

# test sequence
seq = 'ATCGATTGAGCTCTAGCGGCTAACTCGAGATCGCtcgatctacgggagtggaccggagacgagtcgaagctttcttgggaactagtcttctgtt'
print(len(seq))
seq = seq.lower()
print(seq)
seqs = [seq[i:i+4] for i in range(0, len(seq), 4)]
print(seqs)
seq = seq.replace('c', '00').replace('g','01').replace('a','10').replace('t','11')
print(seq)
seqs = [seq[i:i+8] for i in range(0, len(seq), 8)]
print(seqs)
