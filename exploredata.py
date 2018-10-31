import readdata

dataLocation = "HA_t_complete_some.1.fasta"
dataobj = readdata.readData(dataLocation)
x,y = dataobj.sepDataLabels()

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


special = []
anyc = 0
for p in x:
    for c in p:
        if c == "X":
            anyc += 1
        if c not in alphabet:
            print(c)
            special.append(c)

print(dataobj.dataToPhoc(x[0:1],5))

'''
your_string = x[0]
l = 2
n = round((len(your_string)+0.1)/2.0)
parts = [your_string[i:i+n] for i in range(0, len(your_string), n)]
print(parts)
'''