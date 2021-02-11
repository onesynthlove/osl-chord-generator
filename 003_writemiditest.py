from music21 import *


cMinor = chord.Chord(["C4", "G4", "E-5"])
cMinor.durationType = "half"


exportStream = stream.Stream()
exportStream.append(cMinor);

exportStream.write("midi", "test003.mid")
        

