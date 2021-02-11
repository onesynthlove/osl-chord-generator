from music21 import *

baseKey = "C"
baseNoteLength = "whole"
exportStream = stream.Stream()

def writeChordsToMainStream(c1 = "i",c2 = "i",c3 = "i",c4 ="i") :
    print("WriteChordsToMainStream")
    h1 = roman.RomanNumeral(c1)
    h2 = roman.RomanNumeral(c2)
    h3 = roman.RomanNumeral(c3)
    h4 = roman.RomanNumeral(c4)
    h1.durationType = "whole"
    h1.key = baseKey 
    h2.durationType = baseNoteLength
    h2.key = baseKey
    h3.durationType = baseNoteLength
    h3.key = baseKey
    h4.durationType = baseNoteLength
    h4.key = baseKey

    h1.quarterLength = 4
    h2.quarterLength = 4
    h3.quarterLength = 4
    h4.quarterLength = 4

    h1.writeAsChord = True
    h2.writeAsChord = True
    h3.writeAsChord = True
    h4.writeAsChord = True
    print("creating new stream")

    exportStream.append(h1)
    exportStream.append(h2)
    exportStream.append(h3)
    exportStream.append(h4)
    return

for chord1 in range(1, 7):
    for chord2 in range(1,7):
        for chord3 in range(1,7):
            for chord4 in range(1,7):
                writeChordsToMainStream(chord1, chord2, chord3, chord4)




print("writing stream")
exportStream.write("midi", "/mnt/c/Users/duke/Downloads/test010.mid")
        

