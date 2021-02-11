import os.path
from music21 import *
from os import path


baseKey = "C"
baseNoteLength = "whole"
baseMidiDirectory = "c:\Users\duke\Downloads\OSL_BeatPatterns\"

def writeStreamPatternToMidiFile(_stream) :
    print("Write Pattern To Midi File")

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
