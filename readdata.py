#a class for reading the data from fasta files
#assumes the following tags: ["name","host","admantane","oseltamivir","increasedvirulence","enhancedtransmission","fasta"]

class readData:
    def __init__(self, location, args = ["name","host","admantane","oseltamivir","increasedvirulence","enhancedtransmission","fasta"]):
        data = open(location,"r")
        lines = data.readlines()
        dataObject = [] #this is gonna contain all the data
        for line in lines: #for every line in the lines of the input file
            line = line[1:] #the first character is always > so redundant
            entry = dict() #create a new dictionary matchint tag as key with value as value
            for arg in args: #for every argument arg is a label in args
                line, part = self.readPart(line) #read the first label called part, and save the rest of the line in line
                entry[arg] = part #save the first label part under the key called arg
            dataObject.append(entry) #add that entry to the dataobject
        self.dataObject = dataObject #set the dataobject to this class

    def readPart(self, line):
        part = ""
        for i in range(len(line)):
            c = line[i]
            if c == '|':
                return (line[i+1:],part)
            if c == '\n':
                return ("",part)
            part += c
    
    def getData(self):
        return self.dataObject

    def cleanName(self):
        for data in self.dataObject:
            if "name" in data:
                data["name"] = data["name"]

    def cleanHost(self):
        for data in self.dataObject:
            if "host" in data:
                data["host"] = data["host"]
    
    def cleanHuman(self):
        for data in self.dataObject:
            if "host" in data:
                if not data["host"] == "Human":
                    data["host"] = "not Human"

    def cleanAdmantane(self):
        for data in self.dataObject:
            if "admantane" in data:
                changed = False
                if data["admantane"] == "AdmantaneResistance_Yes":
                    changed = True
                    data["admantane"] = 1
                if data["admantane"] == "AdmantaneResistance_No":
                    changed = True
                    data["admantane"] = 0
                if data["admantane"] == "AdmantaneResistance_Segment/protein_not_present" or data["admantane"] == "AdmantaneResistance_" or data["admantane"] == "AdmantaneResistance_Unknown":
                    changed = True
                    data["admantane"] = -1
                if not changed:
                    print("Unexpected label in admantane: " + str(data["admantane"]))
    
    def cleanOseltamivir(self):
        for data in self.dataObject:
            if "oseltamivir" in data:
                changed = False
                if data["oseltamivir"] == "OseltamivirResistance_Yes":
                    changed = True
                    data["oseltamivir"] = 1
                if data["oseltamivir"] == "OseltamivirResistance_No":
                    changed = True
                    data["oseltamivir"] = 0
                if data["oseltamivir"] == "OseltamivirResistance_Segment/protein_not_present" or data["oseltamivir"] == "OseltamivirResistance_" or data["oseltamivir"] == "OseltamivirResistance_Unknown":
                    changed = True
                    data["oseltamivir"] = -1
                if not changed:
                    print("Unexpected label in oseltamivir: " + str(data["oseltamivir"]))

    def cleanVirulence(self):
        for data in self.dataObject:
            if "increasedvirulence" in data:
                changed = False
                if data["increasedvirulence"] == "IncreasedVirulence_Yes":
                    changed = True
                    data["increasedvirulence"] = 1
                if data["increasedvirulence"] == "IncreasedVirulence_No":
                    changed = True
                    data["increasedvirulence"] = 0
                if data["increasedvirulence"] == "IncreasedVirulence_Segment/protein_not_present" or data["increasedvirulence"] == "IncreasedVirulence_" or data["increasedvirulence"] == "IncreasedVirulence_Unknown":
                    changed = True
                    data["increasedvirulence"] = -1
                if not changed:
                    print("Unexpected label in increasedvirulence: " + str(data["increasedvirulence"]))

    def cleanTransmission(self):
        for data in self.dataObject:
            if "enhancedransmission" in data:
                changed = False
                if data["enhancedtransmission"] == "EnhancedTransmission_Yes":
                    changed = True
                    data["enhancedtransmission"] = 1
                if data["enhancedtransmission"] == "EnhancedTransmission_No":
                    changed = True
                    data["enhancedtransmission"] = 0
                if data["enhancedtransmission"] == "EnhancedTransmission_Segment/protein_not_present" or data["enhancedtransmission"] == "EnhancedTransmission_" or data["enhancedtransmission"] == "EnhancedTransmission_Unknown":
                    changed = True
                    data["enhancedtransmission"] = -1
                if not changed:
                    print("Unexpected label in enhancedtransmission: " + str(data["enhancedtransmission"]))
    
    def cleanAll(self):
        self.cleanName()
        self.cleanHost()
        self.cleanAdmantane()
        self.cleanOseltamivir()
        self.cleanVirulence()
        self.cleanTransmission()

    def sepDataLabels(self):
        data = []
        labels = []

        for line in self.dataObject:
            data.append(line.pop("fasta"))
            labels.append(line)

        return (data, labels)

    def dataToSqPhoc(self,data,level):
        phocs = []
        for p in data: #for datapoint p in dataset data
            phoc = []
            parts = self.makeParts(p,level) #get the parts for phoc
            parts = [item for sublist in parts for item in sublist] #flatten the array
            for part in parts: #for each (sub)string part in list of split up strings parts
                phoc += self.makeHist(part)
            phocs.append(phoc)
        return phocs

    def dataToPhoc(self,data,level):
        phocs = []
        for p in data: #for datapoint p in dataset data
            phoc = []
            parts = self.makeParts(p,level) #get the parts for phoc
            parts = [item for sublist in parts for item in sublist] #flatten the array
            for part in parts: #for each (sub)string part in list of split up strings parts
                phoc += self.makeHist(part)
            phocs.append(phoc)
        return phocs

    def makeHist(self,p):
        hist = [0] * 26
        for c in p: #for character c in datapoint p
            v = ord(c) #integer value v of character c
            v -= 65 #character "A" should be indexed at 0
            if v < 0 or v > 25: #if value v is outside of alphabet range
                print("Error: character " + c + " is not an uppercase alphabetical letter.")
                return -1
            hist[v] += 1
        return hist

    #needs to change based on actual phoc, now it's kind of a messy square phoc
    def makeParts(self,p,level):
        parts = [None] * level
        parts[0] = [p]

        for i in range(1,level):
            parts[i] = self.splitStrings(parts[i-1])

        return parts

    def splitStrings(self,strings):
        part = []

        for s in strings: #for string s in strings
            n = round((len(s)+0.1)/2.0)
            part += [s[i:i+n] for i in range(0, len(s), n)]

        return part