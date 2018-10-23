class readData:
    def __init__(self, location, *args):
        data = open(location,"r")
        lines = data.readlines()
        dataObject = []
        for line in lines:
            entry = dict()
            for arg in args:
                line, part = self.readPart(line)
                entry[arg] = part
            dataObject.append(entry)
        self.dataObject = dataObject

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
                data["name"] = data["name"][1:]

    def cleanHost(self):
        for data in self.dataObject:
            if "host" in data:
                data["host"] = data["host"]

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