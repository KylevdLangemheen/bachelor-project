#translate the supplied data format into preferred format
sourceName = "HA_complete_human.fasta"        #source file to read
goalName = "HA_t_complete_human.fasta"        #goal file to write

sourceFile = open(sourceName,"r")
goalFile = open(goalName,"w")

nextLabel = True
FASTA = ""
for line in sourceFile:
    if nextLabel:
        FASTA = FASTA + line.rstrip("\n") + "|"
        nextLabel = False
    else:
        FASTA = FASTA + line.rstrip("\n")
    if line == "\n":
        goalFile.write(FASTA + "\n")
        FASTA = ""
        nextLabel = True
