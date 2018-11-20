import readdata

#redundant! encoding should be done during the input phase, rather than encoding the entire file.

#a file for onehot encoding of the fasta dataset!
#dimensions: each row is a datapoint. Starts with an ID, then a 2D array of one hot encoded fasta characters, then potential labels.
#example:   encoded[n][0]       returns the nth ID
#example:   encoded[n][1]       returns the nth array of onehots
#example:   encoded[n][1][c]    returns the cth one-hot encoded character of the nth array of onehots
#example:   encoded[n][2]       returns the nth array of labels
#example:   encoded[n][2][l]    returns the lth label of the nth array of labels


def oneHot(c):
    onehot = [0] * 26
    onehot[ord(c)-65] = 1
    return onehot

def encode1(x):
    onehots = []
    for c in x:
        onehots.append(oneHot(c))
    return onehots

def getEncoded(dataLocation = "fakefasta.fasta"):
    dataobj = readdata.readData(dataLocation,["host","fasta"])
    dataobj.cleanHost()
    xfull,yfull = dataobj.sepDataLabels()

    encoded = []
    for i in range(len(xfull)):
        encode = []
        encode.append(i)  #add id

        encode.append(encode1(xfull[i])) #add onehots

        labels = []
        for key in yfull[i]:
            label = yfull[i][key]
            labels.append(label)
        encode.append(labels) #add labels
        encoded.append(encode)
    return encoded

def writeEncoded(dataLocation = "fakefasta_encoded.fasta",encoded = getEncoded()):
    f = open(dataLocation,"w")
    for line in encoded:
        sentence = ""
        sentence += str(line[0]) + "|"
        for part in line[1]:
            sentence += str(part).replace(",", "")[1:-1] + ","
        sentence = sentence[:-1]

        sentence += "|"
        for part in line[2]:
            sentence += part + ","
        sentence = sentence[:-1]

        sentence += "\n"
        f.write(sentence)
    f.close()

def readEncoded(dataLocation = "fakefasta_encoded.fasta"):
    f = open(dataLocation,"r")
    encoded = []
    for line in f.readlines():
        encode = []
        line = line[:-1]
        parts = line.split("|")
        encode.append(int(parts[0]))
        onehotparts = parts[1].split(",")
        onehots = []
        for onehot in onehotparts:
            onehots.append([int(s) for s in onehot.split(' ')])
        encode.append(onehots)
        labelstrings = parts[2].split(",")
        labels = []
        for label in labelstrings:
            labels.append(label)
        encode.append(labels)
        encoded.append(encode)
    return encoded
