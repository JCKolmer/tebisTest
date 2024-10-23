#file bearbeiten, text datei in Array aus integer arrays machen die jede Zeile repräsentieren
file = input("Enter filepath:")
with open(file) as f:
    contents = f.readlines()
    arrayofArrays = []
    for x in contents:
        array = x.split()
        numarray = []
        for i in array:
            numarray.append(int(i))        
        arrayofArrays.append(numarray)

aktZeile = len(arrayofArrays) - 2
while aktZeile > 0:
    n = 0
    while n < len(arrayofArrays[aktZeile]):
        arrayofArrays[aktZeile][n] = arrayofArrays[aktZeile][n]  + max(arrayofArrays[aktZeile+1][n], arrayofArrays[aktZeile+1][n+1])
        n += 1
    aktZeile -= 1
ergebnis = arrayofArrays[0][0] + max(arrayofArrays[1][0],arrayofArrays[1][1])
print(ergebnis)
