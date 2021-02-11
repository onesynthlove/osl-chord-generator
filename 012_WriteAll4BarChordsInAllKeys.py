import os.path
from music21 import *
from os import path


baseKey = "C"
baseNoteLength = "whole"
baseMidiDirectory = "/mnt/c/Users/duke/Downloads/DWWMidi_ChordProgressions/" 

def writeChordsToMidiFile(c1 = "i",c2 = "i",c3 = "i",c4 ="i") :
    print("WriteChordsToMainStream")
    exportStream = stream.Stream()

    # default to mjor 7 diminished
    if c1 == 7:
        c1 = "VII"
    if c2 == 7:
        c2 = "VII"
    if c3 == 7:
        c3 = "VII"
    if c4 == 7:
        c4 = "VII"

    print("the value of c1 is " + str(c1))
    print("the value of c2 is " + str(c2))
    print("the value of c3 is " + str(c3))
    print("the value of c4 is " + str(c4))
    
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
    
    filePath = baseMidiDirectory + baseKey + "-" + h1.figure + "-" + h2.figure + "-" + h3.figure + "-" + h4.figure + ".mid"
    if path.exists(filePath) != True:
        print("writing stream for progression " + filePath )
        exportStream.write("midi", filePath)
    else:
        print(filePath + " already exists. Skipping write operation.")
    return
    
# keysIteration = ["C#", "D", "E-", "E", "F", "G-", "G", "A-", "A", "B-", "B", "C"] 
keysIteration = ["E-", "E", "F", "G-", "G", "A-", "A", "B-", "B", "C"] 

for currentKey in keysIteration:
    baseKey = currentKey
    for chord1 in range(1, 8):
        for chord2 in range(1,8):
            for chord3 in range(1,8):
                for chord4 in range(1,8):
                    writeChordsToMidiFile(chord1, chord2, chord3, chord4)
                    # exportStream.write("midi", "/mnt/c/Users/duke/Downloads/DWW_ChordProgressions/" +  + ".mid")



        

