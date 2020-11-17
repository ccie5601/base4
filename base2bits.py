seq = 'ATCGATTGAGCTCTAGCGGCTAACTCGAGATCGCtcgatctacgggagtggaccggagacgagtcgaagctttcttgggaactagtcttctgtt'
print(len(seq))
print(len(seq)/4)
seq = seq.lower()
print(seq)
seqs = [seq[i:i+4] for i in range(0, len(seq), 4)]
print(seqs)
seq = seq.replace('c', '00').replace('g','01').replace('a','10').replace('t','11')
print(seq)
seqs = [seq[i:i+8] for i in range(0, len(seq), 8)]
print(seqs)
