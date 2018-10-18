import os
sourceName = "HA_complete_all.fasta"        #source file to read
goalName = "HA_t_complete_all.fasta"        #goal file to write

sourceFile = open(sourceName,"r")
goalFile = open(goalName,"w")

nextLabel = True
FASTA = ""
for line in sourceFile:
    if nextLabel:
        goalFile.write(FASTA)
        FASTA = ""
        goalFile.write(line)
        nextLabel = False
    else:
        FASTA = FASTA + line.rstrip("\n")
