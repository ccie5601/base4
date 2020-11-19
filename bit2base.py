# open a converted base to bits file and convert it back to the base sequences

seq2 = ''
with open('chr01.txt') as a:
    while 1:
        seq = a.read(2)
        # print(seq)
        seq = seq.replace('00', 'c').replace('01', 'g').replace('10', 'a').replace('11', 't')
        seq2 += seq
        if not seq:
            break

print(len(seq2))
print(seq2)
