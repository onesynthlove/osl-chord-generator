from music21 import *


h1 = harmony.ChordSymbol("Cm")
h2 = harmony.ChordSymbol("Em")
h3 = harmony.ChordSymbol("G")
h4 = harmony.ChordSymbol("Em")
h1.durationType = "whole"
h2.durationType = "whole"
h3.durationType = "whole"
h4.durationType = "whole"

h1.quarterLength = 4
h2.quarterLength = 4
h3.quarterLength = 4
h4.quarterLength = 4


h1.writeAsChord = True
h2.writeAsChord = True
h3.writeAsChord = True
h4.writeAsChord = True


print("built the harmony objects")

exportStream = stream.Stream()


print("creating new stream")


exportStream.append(h1)
exportStream.append(h2)
exportStream.append(h3)
exportStream.append(h4)


print("writing stream")
exportStream.write("midi", "/mnt/c/Users/duke/Downloads/test006.mid")
        

