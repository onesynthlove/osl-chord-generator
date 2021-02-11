from music21 import *


cMinor = chord.Chord(["C4", "G4", "E-5"])
cMinor.durationType = "whole"


eMinor = chord.Chord(["E4","G4","B4"])
eMinor.durationType = "whole"


exportStream = stream.Stream()
exportStream.append(cMinor)
exportStream.append(eMinor)


exportStream.write("midi", "test004.mid")
        

