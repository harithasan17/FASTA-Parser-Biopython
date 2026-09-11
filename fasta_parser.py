from Bio import SeqIO

fasta_file = "sample.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    sequence = str(record.seq)

    sequence_length = len(sequence)

    gc_count = sequence.upper().count("G") + sequence.upper().count("C")

    gc_content = (gc_count / sequence_length) * 100

    print("ID:", record.id)
    print("Length:", sequence_length)
    print("GC Content: {:.2f}%".format(gc_content))
    print("-" * 30)
